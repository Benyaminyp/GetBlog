document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('input[name="q"]'); // این فیلد برای جستجو است
    if (searchInput) {
        searchInput.setAttribute('placeholder', 'جستجو بر اساس موضوع');
    }
});