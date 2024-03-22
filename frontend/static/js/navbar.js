document.querySelector('.menu-icon').addEventListener('click', function() {
    this.classList.toggle('active');
    const overlay = document.querySelector('#menuOverlay');
    if (overlay.classList.contains('hidden')) {
        overlay.classList.remove('hidden');
        setTimeout(() => overlay.classList.remove('-translate-x-full'), 10); // Delay needed to apply transition effect from the initial state
    } else {
        overlay.classList.add('-translate-x-full');
        setTimeout(() => overlay.classList.add('hidden'), 300); // Match the duration of the transition
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const navbarEnd = document.getElementById('navbarEnd');
    const token = localStorage.getItem('jwtToken');

    if (token) {
        navbarEnd.innerHTML = `
        <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-sm avatar">
          <div class="w-10 rounded-full shadow">
            <img alt="Tailwind CSS Navbar component" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
          </div>
        </div>
        <ul tabindex="0" class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
          <li>
            <a class="justify-between">
              Profile
              <span class="badge">New</span>
            </a>
          </li>
          <li><a>Settings</a></li>
          <li><a>Logout</a></li>
        </ul>
      </div>    
        `;
    } else {
        navbarEnd.innerHTML = `
        <div class="flex gap-8">
            <button href="/register" class="btn btn-ghost btn-sm w-24 hidden md:block text-lg text-text ">Register</button>
            <button href="/login" class="btn btn-secondary btn-sm shadow w-24 hidden md:block text-text text-lg">Login</button>
            <a href="/account" class="btn btn-ghost md:hidden flex justify-center items-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6 svg-text">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"/>
                </svg>
          
            </a>
        </div>`;
    }
});
