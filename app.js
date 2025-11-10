
// Minimal enhancement: click exhibit chip to flash the nearest mini chart panel
document.querySelectorAll('.chip').forEach(function(chip){
  chip.addEventListener('click', function(){
    var panel = chip.closest('.panel').querySelector('svg')?.parentElement;
    if(panel){
      panel.style.boxShadow = '0 0 0 2px var(--accent)';
      setTimeout(()=> panel.style.boxShadow='none', 800);
    }
  });
});
