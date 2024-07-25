// const translations = {
//     en: {
//         mainWebSite: "Main website",
//         intro: "This is an example of a multilingual website."
//     },
//     ru: {
//         mainWebSite: "Основной сайт",
//         intro: "Это пример мультиязычного сайта."
//     },
//     ar: {
//         mainWebSite: "الموقع الرئيسي",
//         intro: "هذا مثال على موقع متعدد اللغات."
//     },
//     zh: {
//         mainWebSite: "主要网站",
//         intro: "这是一个多语言网站的示例。"
//     }
// };
//
// function changeLanguage(lang) {
//     const translatableElements = document.querySelectorAll('.translatable');
//
//     translatableElements.forEach(element => {
//         const key = element.getAttribute('data-key');
//         if (translations[lang][key]) {
//             element.textContent = translations[lang][key];
//         }
//     });
// }
//
// document.getElementById('ru').onclick = function() { changeLanguage('ru'); };
// document.getElementById('en').onclick = function() { changeLanguage('en'); };
// document.getElementById('ar').onclick = function() { changeLanguage('ar'); };
// document.getElementById('zh').onclick = function() { changeLanguage('zh'); };
//
// changeLanguage('en');
