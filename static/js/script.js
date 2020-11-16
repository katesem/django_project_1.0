


document.getElementById('clear-button').addEventListener('click', function () {
  ["option1", "option2", "option3","option4" ].forEach(function(id) {
    document.getElementById(id).checked = false;
  });
  return false;
})

/*
function selectOnlyThis(id) {
  for (var i = 1;i <= 4; i++)
  {
      document.getElementById("check" + i).checked = false;
  }
  document.getElementById(id).checked = true;
  
}
*/