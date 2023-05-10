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

	// Delete button
	const delete_profile = document.querySelector('#delete-profile');

	// Modal for pop up messages
	const modal = document.querySelector('.modal');
	const modal_confirm = document.querySelector('#modal-confirm');
	const modal_message = document.querySelector('#modal-message');
	const modal_close = document.querySelector('#modal-close');

	const parameter_label = document.querySelectorAll('.parameter-label');

	// Functions
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
				let percent = (100 * parseFloat(plan.progress)) / parseFloat(plan.goal);
				element.innerText = Math.round(percent) + '%';

				if (percent >= 100) {
					bar.style.width = '100%';
				} else {
					bar.style.width = percent + '%';
				}
			});
	};

	// Percentage per category per date
	const load_weekly_progress = (bar, percentage) => {
		if (parseFloat(percentage.innerText) > 100) {
			bar.style.height = 0 + '%';
		} else {
			bar.style.height = 100 - percentage.innerText + '%';
		}

		percentage.innerText = percentage.innerText + '%';
	};

	// Toggle between divs
	if (document.location.href.includes('plan/progress')) {
		progress_toggle();
	} else if (document.location.href.includes('plan/goals')) {
		goals_toggle();
	} else if (document.location.href.includes('plan/weekly')) {
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
	if (progress_link) {
		progress_link.addEventListener('click', () => {
			document.location.href = `/plan/progress/${progress_date.value}`;
		});
	}

	if (goals_link) {
		goals_link.addEventListener('click', () => {
			document.location.href = `/plan/goals/${goals_date.value}`;
		});
	}

	if (weekly_link) {
		weekly_link.addEventListener('click', () => {
			document.location.href = `/plan/weekly/${goals_date.value}`;
		});
	}

	if (progress_date) {
		progress_date.addEventListener('change', () => {
			document.location.href = `/plan/progress/${progress_date.value}`;
		});
	}

	if (goals_date) {
		goals_date.addEventListener('change', () => {
			document.location.href = `/plan/goals/${goals_date.value}`;
		});
	}

	if (weekly_date) {
		weekly_date.addEventListener('change', () => {
			document.location.href = `/plan/weekly/${weekly_date.value}`;
		});
	}

	if (delete_profile) {
		delete_profile.addEventListener('click', (event) => {
			event.preventDefault();
			modal.classList.toggle('hidden');
			modal_message.innerText = 'Do you want to delete your profile?';
		});

		modal_confirm.addEventListener('click', (event) => {
			event.preventDefault();
			document.location.href = '/delete-profile';
		});
	}

	if (modal_close) {
		modal_close.addEventListener('click', (event) => {
			event.preventDefault();
			modal.classList.toggle('hidden');
		});
	}

	parameter_label.forEach((label) => {
		const parameter_input =
			label.parentElement.querySelector('.parameter-input');
		if (
			(label && label.dataset.category === 'Water_Intake') ||
			(label && label.dataset.category === 'Sleep')
		) {
			label.style.display = 'none';
			parameter_input.style.display = 'none';
		}
	});
});
