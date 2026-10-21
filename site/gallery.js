const search = document.querySelector('#search');
const category = document.querySelector('#category');
const origin = document.querySelector('#origin');
const cards = [...document.querySelectorAll('.card')];
function filter() {
  const query = search.value.trim().toLocaleLowerCase();
  let visible = 0;
  for (const card of cards) {
    const match = (!category.value || card.dataset.category === category.value) && (!origin.value || card.dataset.origin === origin.value) && card.dataset.search.toLocaleLowerCase().includes(query);
    card.hidden = !match;
    if (match) visible++;
  }
  document.querySelector('#count').textContent = `${visible} / ${cards.length} prompts`;
  document.querySelector('#empty').hidden = visible !== 0;
}
search.addEventListener('input', filter);
category.addEventListener('change', filter);
origin.addEventListener('change', filter);
