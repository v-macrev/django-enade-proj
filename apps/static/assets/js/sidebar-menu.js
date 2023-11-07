document.addEventListener('DOMContentLoaded', function() {
  const iconNavbarSidenav = document.getElementById('iconNavbarSidenav');
  const body = document.getElementsByTagName('body')[0];
  const navbar = document.getElementsByClassName('navbar')[0]; // Assuming there's only one navbar

  iconNavbarSidenav.addEventListener('click', function() {
    body.classList.toggle('g-sidenav-pinned');
    body.classList.toggle('g-sidenav-hidden');
  });
});
