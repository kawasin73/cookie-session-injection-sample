function getInvalid() {
  console.log("getInvalid");
  fetch('/value').then(function(response) {
    return response.text()
  }).then(function(body) {
    console.log("getInvalid :", body);
  });
}
