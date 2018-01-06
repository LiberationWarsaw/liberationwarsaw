function filterAllEvents() {
  var unselected_events = document.querySelectorAll('.event-page-item');
  for (i = 0; i < unselected_events.length; i++) {
    unselected_events[i].classList.add('inactive');
  }
}

function clearFilters() {
  var unselected_events = document.querySelectorAll('.event-page-item');
  for (i = 0; i < unselected_events.length; i++) {
    unselected_events[i].classList.remove('inactive');
  }
}

function filterEvents(query) {
  filterAllEvents();
  var selected_events = document.querySelectorAll(query);
    for (i = 0; i < selected_events.length; i++) {
      selected_events[i].classList.toggle('inactive');
    }
  }
