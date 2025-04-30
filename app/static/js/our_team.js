function showEmployees(svgElement, contentElement) {
    let rotated = false;

    return function () {
        rotated = !rotated;

        if (rotated) {
            svgElement.style.transform = 'rotate(180deg)';
            contentElement.style.display = 'grid';
        } else {
            svgElement.style.transform = 'rotate(0deg)';
            contentElement.style.display = 'none';
        }
    };
}

// Select the leader container
const containerLeader = document.getElementById('contenedor-svg-1');
const svgLeader = containerLeader.querySelector('svg');
const showPhotoLeader = document.getElementById('photo-employees-1'); 


// Select the architects and engineers
const containerArchitectsEngineers = document.getElementById('contenedor-svg-2');
const svgArchitectsEngineers = containerArchitectsEngineers.querySelector('svg');
const showPhotoArchitectsEngineers = document.getElementById('photo-employees-2');

// Select the general team
const containerGeneralTeam = document.getElementById('contenedor-svg-3');
const svgGeneralTeam = containerGeneralTeam.querySelector('svg');
const showPhotoGeneralTeam = document.getElementById('photo-employees-3');

const showLeaders = showEmployees(svgLeader, showPhotoLeader);
const showArchitectsEngineers = showEmployees(svgArchitectsEngineers, showPhotoArchitectsEngineers);
const showGeneralTeam = showEmployees(svgGeneralTeam, showPhotoGeneralTeam);

containerLeader.addEventListener('click', showLeaders);
containerArchitectsEngineers.addEventListener('click', showArchitectsEngineers);
containerGeneralTeam.addEventListener('click', showGeneralTeam);
