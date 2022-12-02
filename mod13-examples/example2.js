'use strict';

// old school promisen käsittely
/**
function responseOK(response) {
  console.log('response', response);
  response.json().then(function (data) {
    console.log('response data', data);
    // datan käsittely tänne
  });
}
function networkError(error) {
  console.error('Pieleen meni', error);
}
const response = fetch('http://localhost:5000/airport/efhk')
  .then(responseOK)
  .catch(networkError);
console.log(response);
console.log('ohjelma jatkuu');
*/

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
  // Kysymysmerkillä vältettäisiin error, jos name-ominaisuutta ei ole olemassa datassa
  // (= undefined) ja yritetään käyttää sen ominaisuuksia (esim. length)
  //if (data.name?.length > 6) {
  //  console.log('nimen pituus yli kuusi');
  //}
  if (data.Error) {
    console.log(data.Error);
    targetElem.innerText = data.Error;
  } else {
    //console.log('results', data);
    const p = document.createElement('p');
    p.textContent = '  Lentokenttä löytyi: ' + data.name;
    targetElem.append(p);
    // disclaimer: nippelitietoa
    // innerText ei näytä välilyöntejä html:ään rendatun text-noden alussa
    //console.log(p.innerText);
    //console.log(p.textContent);
  }
}

// pääohjelma main() on asynkroninen, koska se käyttää await:ia kutsuessaa muita
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