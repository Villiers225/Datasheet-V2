document.addEventListener('click', function(e){
  const chip = e.target.closest('.chip');
  if(!chip) return;
  const fig = chip.closest('li')?.querySelector('figure');
  if(fig){
    fig.style.boxShadow='0 0 0 2px var(--accent)';
    setTimeout(()=> fig.style.boxShadow='none', 800);
  }
});