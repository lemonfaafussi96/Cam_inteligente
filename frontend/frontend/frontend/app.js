async function generateRap() {
  const profile = {
    name: document.getElementById('name').value,
    age: document.getElementById('age').value,
    classe: document.getElementById('classe').value,
    studyTime: document.getElementById('studyTime').value,
    environment: document.getElementById('environment').value,
    passion: document.getElementById('passion').value
  };

  const matiere = document.getElementById('matiere').value;
  const coursText = document.getElementById('coursText').value;

  const response = await fetch(`http://localhost:8000/transform`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: coursText, matiere: matiere, profil: profile })
  });

  const data = await response.json();

  document.getElementById('rapTextDisplay').innerText = data.rapText;
  document.getElementById('audioResult').src = data.audioUrl;
}
