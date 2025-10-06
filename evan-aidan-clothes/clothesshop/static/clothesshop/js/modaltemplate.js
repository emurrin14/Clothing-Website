const openBtn = document.getElementById('openModalBtn');
const modal = document.getElementById('Modal');
const closeBtn = document.getElementById('closeModalBtn');

function showModal() {
  modal.setAttribute('aria-hidden', 'false');
  closeBtn.focus();
}

function hideModal() {
  modal.setAttribute('aria-hidden', 'true');
  openBtn.focus();
}

openBtn.addEventListener('click', showModal);

closeBtn.addEventListener('click', hideModal);

window.addEventListener('click', (e) => {
  if (e.target === modal) {
    hideModal();
  }
});
