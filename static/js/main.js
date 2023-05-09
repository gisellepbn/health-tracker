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

	// Percentage per plan per date
	const load_plan_percentage = (element, bar, plan_date, plan_id) => {
		fetch(`/plan/progress/${plan_date}/${plan_id}`)
			.then((response) => response.json())
			.then((plan) => {
				element.innerText =
					(100 * parseFloat(plan.progress)) / parseFloat(plan.goal) + '%';

				bar.style.width =
					(100 * parseFloat(plan.progress)) / parseFloat(plan.goal) + '%';
			});
	};

	// Percentage per category per date
	const load_weekly_progress = (bar, percentage) => {
		bar.style.height = 100 - percentage.innerText + '%';
		percentage.innerText = percentage.innerText + '%';
	};

	// Toggle between divs
	if (document.location.href.includes('progress')) {
		progress_toggle();
	} else if (document.location.href.includes('goals')) {
		goals_toggle();
	} else {
		weekly_toggle();
	}

	// Load percentage of goal reached per plan
	const plan_percentage = document.querySelectorAll('.plan_percentage');

	plan_percentage.forEach((percentage) => {
		const bar = percentage.parentElement.querySelector('.bar-done');

		load_plan_percentage(
			percentage,
			bar,
			progress_date.value,
			percentage.dataset.id
		);
	});

	// Load percentage per category per date
	const chart_percentage = document.querySelectorAll('.chart-percentage');

	chart_percentage.forEach((percentage) => {
		const bar = percentage.parentElement.querySelector('.chart-fill');
		load_weekly_progress(bar, percentage);
	});

	// Events Handlers
	progress_link.addEventListener('click', () => {
		document.location.href = `/plan/progress/${progress_date.value}`;
	});

	goals_link.addEventListener('click', () => {
		document.location.href = `/plan/goals/${goals_date.value}`;
	});

	weekly_link.addEventListener('click', () => {
		document.location.href = `/plan/weekly/${goals_date.value}`;
	});

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
