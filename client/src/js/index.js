import {fromEvent} from "rxjs";
import {
  debounceTime,
  map,
  distinctUntilChanged,
  switchMap
} from "rxjs/operators";
import {ajax} from "rxjs/ajax";

const input = document.createElement("input");
input.className = "search";
input.type = "text";

const searchResultsContainer = document.createElement("ul");
searchResultsContainer.className = "search-results-container";

document.body.appendChild(input);
document.body.appendChild(searchResultsContainer);

const url = "http://localhost:5000/messages";

const $input = fromEvent(input, "change").pipe(
  debounceTime(500),
  map(e => e.target.value),
  distinctUntilChanged(),
  switchMap(term =>
    ajax({
      url,
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        prefix: term
      })
    })
  ),
  map(({response}) => response.autoComplete.messages)
);

$input.subscribe(val => {
  removeChildren(searchResultsContainer);
  addElements(searchResultsContainer, val);
});

function addElements(element, results) {
  const searchResults = document.createDocumentFragment();

  results.forEach(result => {
    const searchResult = document.createElement("li");
    searchResult.textContent = result;
    searchResults.appendChild(searchResult);
  });

  element.appendChild(searchResults);
}

function removeChildren(element) {
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}
