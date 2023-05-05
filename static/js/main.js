document.addEventListener('DOMContentLoaded', () => {
	// Divs
	const daily_progress = document.querySelector('#daily-progress');
	const daily_goals = document.querySelector('#daily-goals');
	const weekly_progress = document.querySelector('#weekly-progress');

	// Sidebar links
	const progress_link = document.querySelector('#progress-link');
	const goals_link = document.querySelector('#goals-link');
	const weekly_link = document.querySelector('#weekly-link');

	// Date Icons
	const progress_date = document.querySelector('#progress-date');
	const goals_date = document.querySelector('#goals-date');
	const weekly_date = document.querySelector('#weekly-date');

	const progress_toggle = () => {
		daily_progress.style.display = 'flex';
		daily_goals.style.display = 'none';
		weekly_progress.style.display = 'none';
	};

	const goals_toggle = () => {
		daily_goals.style.display = 'flex';
		daily_progress.style.display = 'none';
		weekly_progress.style.display = 'none';
	};

	const weekly_toggle = () => {
		weekly_progress.style.display = 'flex';
		daily_goals.style.display = 'none';
		daily_progress.style.display = 'none';
	};

	// Toggle between divs
	if (document.location.href.includes('progress')) {
		progress_toggle();
	} else if (document.location.href.includes('goals')) {
		goals_toggle();
	} else {
		weekly_toggle();
	}

	// Events Handlers
	progress_link.addEventListener('click', progress_toggle);
	goals_link.addEventListener('click', goals_toggle);
	weekly_link.addEventListener('click', weekly_toggle);

	progress_date.addEventListener('change', () => {
		document.location.href = `/plan/progress/${progress_date.value}`;
	});

	goals_date.addEventListener('change', () => {
		document.location.href = `/plan/goals/${goals_date.value}`;
	});

	weekly_date.addEventListener('change', () => {
		document.location.href = `/plan/weekly/${weekly_date.value}`;
	});
});
