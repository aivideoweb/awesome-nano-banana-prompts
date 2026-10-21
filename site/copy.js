document.querySelectorAll('[data-copy]').forEach(button => {
  button.addEventListener('click', async () => {
    const status = document.querySelector('#copy-status');
    try {
      await navigator.clipboard.writeText(document.getElementById(button.dataset.copy).textContent);
      status.textContent = 'Copied / 已复制';
    } catch {
      status.textContent = 'Select the prompt text and copy manually / 请选中文字手动复制';
    }
  });
});
