const OWNER = "Fairellxd";
const REPO = "lirik-lagu";
const API = `https://api.github.com/repos/${OWNER}/${REPO}/contents`;

const listEl = document.querySelector("#songList");
const searchEl = document.querySelector("#search");
const countEl = document.querySelector("#count");
const emptyEl = document.querySelector("#empty");
const viewEl = document.querySelector("#lyricsView");
const titleEl = document.querySelector("#songTitle");
const lyricsEl = document.querySelector("#lyrics");
const sourceEl = document.querySelector("#sourceLink");

let songs = [];
let selected = null;

function titleFromFile(name) {
  return name.replace(/\.py$/i, "").replace(/[-_]+/g, " ").replace(/\b\w/g, c => c.toUpperCase());
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
    const res = await fetch(API);
    if (!res.ok) throw new Error(`GitHub API: ${res.status}`);
    const files = await res.json();
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

  try {
    const res = await fetch(song.url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const python = await res.text();
    lyricsEl.textContent = extractLyrics(python) || "Lirik tidak ditemukan di file ini.";
  } catch (err) {
    lyricsEl.textContent = `Gagal memuat lirik: ${err.message}`;
  }
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
