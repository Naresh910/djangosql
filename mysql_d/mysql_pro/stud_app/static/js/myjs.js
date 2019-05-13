var elm = document.getElementById('delete-object');
var objectID = elm.getAttribute('data-object-id');
var resultDiv = document.getElementById('result');
elm.addEventListener('click', function() {
  var ask = confirm('r u sure?');
  if (ask && objectID) {
    var r = "Page will be redirected to </object/delete/" + objectID + "/>";
    resultDiv.textContent = r;
  } else {
    resultDiv.textContent = "User cancelled the dialog box...";
  }
  return false;
});