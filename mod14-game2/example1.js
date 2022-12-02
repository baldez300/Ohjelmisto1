// await-async
async function getAirportData(icao) {
  const response = await fetch('http://localhost:5000/airport/' + icao);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data)
  return data;
}

function renderHtml(data) {
  const targetElem = document.querySelector('#search-result');
  if (data.Error) {
    console.log(data.Error);
    targetElem.innerText = data.Error;
  } else {
    const p = document.createElement('p');
    p.textContent = '  Lentokenttä löytyi: ' + data.name;
    targetElem.append(p);
  }
}

// asynkronisia funktioita
async function main() {
  const userInput = prompt('Mikä kenttä (icao)?');
  // async funktio palauttaa promisen
  const airportData = await getAirportData(userInput);
  console.log('airport data:', airportData);
  renderHtml(airportData);
}

main();
console.log('ohjelma jatkuu');