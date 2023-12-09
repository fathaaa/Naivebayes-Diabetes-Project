function removePlaceholder(input) {
  input.setAttribute('data-placeholder', input.placeholder);
  input.placeholder = '';
}

function restorePlaceholder(input) {
  if (!input.value) {
      input.placeholder = input.getAttribute('data-placeholder');
  }
}

function showPopup(result, probDiabetes, probNoDiabetes) {
  document.getElementById('predictionResult').innerText = result;
  document.getElementById('probabilityDiabetes').innerText = probDiabetes;
  document.getElementById('probabilityNoDiabetes').innerText = probNoDiabetes;
  document.getElementById('resultPopup').style.display = 'block';
  document.querySelector('.overlay').style.display = 'block';
}

function closePopup() {
  document.getElementById('resultPopup').style.display = 'none';
  document.querySelector('.overlay').style.display = 'none';
}
