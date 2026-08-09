const OWNER = "Fairellxd";
const REPO = "lirik-lagu";
const API = `https://api.github.com/repos/${OWNER}/${REPO}/contents`;
const RAW = `https://raw.githubusercontent.com/${OWNER}/${REPO}/main`;

const listEl = document.querySelector("#songList");
const searchEl = document.querySelector("#search");
const countEl = document.querySelector("#count");
const emptyEl = document.querySelector("#empty");
const viewEl = document.querySelector("#lyricsView");
const titleEl = document.querySelector("#songTitle");
const lyricsEl = document.querySelector("#lyrics");
const sourceEl = document.querySelector("#sourceLink");
const audioEl = document.querySelector("#audioPlayer");
const audioStatusEl = document.querySelector("#audioStatus");

let songs = [];
let selected = null;
let audioFiles = new Map();

function titleFromFile(name) {
  return name.replace(/\.py$/i, "").replace(/[-_]+/g, " ").replace(/\b\w/g, c => c.toUpperCase());
}

function baseName(name) {
  return name.replace(/\.[^.]+$/, "").toLowerCase();
}

function renderList(filter = "") {
  const q = filter.trim().toLowerCase();
  const visible = songs.filter(s => s.title.toLowerCase().includes(q) || s.file.toLowerCase().includes(q));
  listEl.innerHTML = "";
  countEl.textContent = `${visible.length} lagu`;

  if (!visible.length) {
    listEl.innerHTML = `<p class="error">Lagu tidak ditemukan.</p>`;
    return;
  }

  visible.forEach(song => {
    const button = document.createElement("button");
    button.className = `song${selected?.file === song.file ? " active" : ""}`;
    button.innerHTML = `<strong>${escapeHtml(song.title)}</strong><small>${escapeHtml(song.file)}</small>`;
    button.addEventListener("click", () => openSong(song));
    listEl.appendChild(button);
  });
}

async function loadSongs() {
  try {
    const [songsRes, audioRes] = await Promise.all([
      fetch(API),
      fetch(`${API}/audio`)
    ]);

    if (!songsRes.ok) throw new Error(`GitHub API: ${songsRes.status}`);
    const files = await songsRes.json();

    if (audioRes.ok) {
      const audio = await audioRes.json();
      audio.filter(f => f.type === "file" && /\.(mp3|ogg|wav|m4a)$/i.test(f.name))
        .forEach(f => audioFiles.set(baseName(f.name), f.download_url));
    }

    songs = files
      .filter(f => f.type === "file" && f.name.toLowerCase().endsWith(".py"))
      .map(f => ({ file: f.name, title: titleFromFile(f.name), url: f.download_url, html: f.html_url }))
      .sort((a, b) => a.title.localeCompare(b.title));
    renderList();
  } catch (err) {
    countEl.textContent = "Gagal memuat";
    listEl.innerHTML = `<p class="error">Tidak bisa mengambil daftar lagu dari GitHub.<br>${escapeHtml(err.message)}</p>`;
  }
}

async function openSong(song) {
  selected = song;
  renderList(searchEl.value);
  emptyEl.hidden = true;
  viewEl.hidden = false;
  titleEl.textContent = song.title;
  sourceEl.href = song.html;
  lyricsEl.textContent = "Memuat...";

  setupAudio(song);

  try {
    const res = await fetch(song.url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const python = await res.text();
    lyricsEl.textContent = extractLyrics(python) || "Lirik tidak ditemukan di file ini.";
  } catch (err) {
    lyricsEl.textContent = `Gagal memuat lirik: ${err.message}`;
  }
}

function setupAudio(song) {
  audioEl.pause();
  audioEl.removeAttribute("src");
  audioEl.load();

  const url = audioFiles.get(baseName(song.file));
  if (!url) {
    audioEl.hidden = true;
    audioStatusEl.hidden = false;
    audioStatusEl.textContent = `Audio belum ada. Upload file dengan nama audio/${baseName(song.file)}.mp3`;
    return;
  }

  audioEl.hidden = false;
  audioStatusEl.hidden = false;
  audioStatusEl.textContent = "Tekan play untuk memutar audio.";
  audioEl.src = url;

  audioEl.play().then(() => {
    audioStatusEl.textContent = "Sedang diputar.";
  }).catch(() => {
    audioStatusEl.textContent = "Browser memerlukan klik tombol play untuk mulai memutar audio.";
  });
}

function extractLyrics(code) {
  const match = code.match(/lyrics\s*=\s*\[(.*?)\]/s);
  if (!match) return "";
  const body = match[1];
  const lines = [];
  const re = /([\"'])(.*?)\1/g;
  let m;
  while ((m = re.exec(body))) {
    lines.push(m[2].replace(/\\n/g, "\n").replace(/\\([\"'])/g, "$1"));
  }
  return lines.join("\n");
}

function escapeHtml(value) {
  return value.replace(/[&<>'"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"}[c]));
}

searchEl.addEventListener("input", e => renderList(e.target.value));
loadSongs();
