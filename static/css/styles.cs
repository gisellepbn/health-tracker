html {
  font-size: 100%;
}

body {
  overflow-x: hidden;
  font-family: "Inter", sans-serif;
  background-color: #f5f5f5;
  color: #f5f5f5;
  scroll-behavior: smooth;
  scroll-padding-top: 5rem;
  transition: 0.2s linear;
}

*::selection {
  background-color: #3f0071;
  color: white;
  font-weight: 400;
}

.text {
  resize: none;
}

li {
  list-style-type: none;
}

h1,
h2,
h3 {
  font-weight: 700;
  color: #2f2e41;
}

h1 {
  font-size: 2.5rem;
}

h2 {
  font-size: 1.5rem;
}

h3 {
  font-size: 1rem;
}

a {
  text-decoration: none;
  font-size: 1rem;
  color: #fb2576;
  cursor: pointer;
}

p {
  font-weight: 400;
  line-height: 1.5rem;
  margin-top: 1rem;
  font-size: 1rem;
  color: #2f2e41;
}

* {
  margin: 0;
  padding: 0;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #150050;
  padding: 1rem 5rem;
  height: 8vh;
}
.navbar .logo {
  color: #f5f5f5;
}
.navbar .logo:hover {
  color: #fb2576;
}
.navbar__items {
  display: flex;
  gap: 1rem;
}
.navbar__items #sign-in {
  color: #f5f5f5;
}
.navbar__items #sign-in:hover {
  color: #fb2576;
  text-decoration: underline;
}
.navbar__items #sign-up {
  color: #fb2576;
}
.navbar__items #sign-up:hover {
  text-decoration: underline;
}
.navbar__items #log-out:hover {
  text-decoration: underline;
}
@media screen and (max-width: 750px) {
  .navbar__items #sign-in {
    font-size: 0.8rem;
    padding-right: 0;
  }
  .navbar__items #sign-up {
    display: none;
  }
}

.btn {
  font-size: 1rem;
  color: white;
  opacity: 80%;
  background-color: #fb2576;
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
.btn:hover {
  background-color: #3f0071;
}

.purple-footer {
  width: 100%;
  height: 32vh;
  display: flex;
  overflow: hidden;
}
.purple-footer .left-skewed {
  width: 50%;
  height: 100%;
  background-color: #3f0071;
  position: relative;
  top: 0;
  left: 0;
  z-index: 0;
  transform: skewY(10deg);
  transform-origin: top left;
}
.purple-footer .right-skewed {
  width: 50%;
  height: 100%;
  background-color: #3f0071;
  position: relative;
  top: 0;
  right: 0;
  z-index: 0;
  transform: skewY(-10deg);
  transform-origin: top right;
}

.white-footer {
  width: 100%;
  height: 32vh;
  display: flex;
  overflow: hidden;
  background-color: #3f0071;
}
.white-footer .left-skewed {
  width: 50%;
  height: 100%;
  background-color: #f5f5f5;
  position: relative;
  top: 0;
  left: 0;
  z-index: 0;
  transform: skewY(10deg);
  transform-origin: top left;
}
.white-footer .right-skewed {
  width: 50%;
  height: 100%;
  background-color: #f5f5f5;
  position: relative;
  top: 0;
  right: 0;
  z-index: 0;
  transform: skewY(-10deg);
  transform-origin: top right;
}

.form {
  width: 25%;
  margin: 4rem auto;
  background-color: #3f0071;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
@media screen and (max-width: 1024px) {
  .form {
    width: 40%;
  }
}
@media screen and (max-width: 480px) {
  .form {
    width: 65%;
  }
}
.form h3,
.form p {
  color: #f5f5f5;
}
.form .form-title {
  font-weight: 300;
  font-size: 1.5em;
}
.form .form-btn {
  width: 100%;
  text-align: center;
}
.form .form-btn:hover {
  background-color: #150050;
}
.form .cta-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.form .cta-group .cta-box {
  display: flex;
  gap: 0.5rem;
}
.form .cta-group .cta-box .update-btn:hover {
  outline: 1px solid #f5f5f5;
}
.form .cta-group .cta-box .cancel-btn {
  background-color: #fafafa;
  padding: 0.4rem 1rem;
  color: #2f2e41;
  outline: 1px solid #f5f5f5;
}
.form .cta-group .cta-box .cancel-btn:hover {
  background-color: transparent;
  color: #f5f5f5;
}
.form .cta-group .delete-btn {
  padding: 0.5rem 1rem;
  background-color: #33658d;
  border-radius: 5px;
}
.form .cta-group .delete-btn:hover {
  background-color: transparent;
  outline: 1px solid #f5f5f5;
}
.form .cta-group .delete-btn i {
  color: #f5f5f5;
}
.form .input {
  font-weight: 100;
  padding: 0.5rem;
  border-radius: 5px;
  border: solid 1px #f5f5f5;
  outline-color: #f5f5f5;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  background-color: #3f0071;
  color: white;
}
.form .input::placeholder {
  color: #f5f5f5;
  font-weight: 100;
}
.form #picture {
  padding-top: 0;
  padding-bottom: 1.5rem;
}

.messages {
  background-color: #3f0071;
  color: #fb2576;
  padding-top: 2rem;
}

.sidebar {
  background-color: #3f0071;
  width: 20vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.sidebar p {
  color: #f5f5f5;
}
.sidebar .profile-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 0;
  width: 100%;
}
.sidebar .profile-box .profile-picture {
  width: 35%;
  height: 35%;
  margin-bottom: 1.5rem;
}
.sidebar .profile-box .profile-picture img {
  width: 100%;
  clip-path: circle();
  background-color: #f5f5f5;
}
.sidebar .profile-box .profile-name {
  font-size: 1.5rem;
  font-weight: 700;
}
.sidebar .profile-box .profile-username {
  margin: 0.5rem 0;
  font-style: italic;
  font-weight: 300;
}
.sidebar .profile-box .profile-edit:hover {
  text-decoration: underline;
}
.sidebar .sidebar-links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.sidebar .sidebar-links .sidebar-link {
  color: #f5f5f5;
}
.sidebar .sidebar-links .sidebar-link:hover {
  color: #fb2576;
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
}
.modal-contents {
  transform: translateY(-80px);
  height: 150px;
  width: 350px;
  background-color: #3f0071;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  color: white;
}
.modal-contents #modal-message {
  font-weight: 400;
  font-size: 1rem;
  color: #f5f5f5;
  margin-top: 0;
}
.modal-contents #modal-confirm {
  font-size: 0.7rem;
}
.modal-contents #modal-confirm:hover {
  outline: 1px solid #f5f5f5;
  background-color: transparent;
}
.modal-contents #modal-close {
  color: #f5f5f5;
  align-self: flex-end;
}
.modal-contents #modal-close:hover {
  color: #fb2576;
}

.hidden {
  display: none !important;
}

.hero-section {
  display: flex;
  flex-direction: "row";
  height: 60vh;
}
.hero-section__text {
  width: 50%;
  justify-self: flex-end;
  align-self: center;
  padding-left: 5rem;
  padding-right: 2rem;
}
.hero-section__text .hero__title {
  font-size: 3rem;
  color: #150050;
}
.hero-section__text .hero__subtitle {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  line-height: 1.5;
  opacity: 80%;
  max-width: 90%;
}
@media screen and (max-width: 960px) {
  .hero-section__text {
    padding-right: 0;
  }
  .hero-section__text .hero__title {
    font-size: 2rem;
  }
  .hero-section__text .hero__subtitle {
    font-size: 1.2rem;
    max-width: 100%;
  }
}
@media screen and (max-width: 750px) {
  .hero-section__text {
    width: 100%;
    padding-right: 5rem;
  }
  .hero-section__text .hero__title {
    font-size: 1.5rem;
  }
  .hero-section__text .hero__subtitle {
    font-size: 1rem;
    max-width: 100%;
  }
  .hero-section__text #cta-btn {
    font-size: 0.8rem;
  }
}
.hero-section__image {
  width: 50%;
}
@media screen and (max-width: 960px) {
  .hero-section__image {
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
.hero-section__image .image-container {
  margin-top: 2rem;
  margin-left: 5rem;
  position: relative;
  z-index: 2;
}
.hero-section__image .image-container .hero-image {
  width: 80%;
  height: 80%;
}
@media screen and (max-width: 960px) {
  .hero-section__image .image-container {
    margin-right: 4rem;
  }
  .hero-section__image .image-container .hero-image {
    width: 100%;
    height: 100%;
  }
}
@media screen and (max-width: 750px) {
  .hero-section__image .image-container {
    display: none;
  }
}
@media screen and (max-width: 750px) {
  .hero-section {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
}

.container {
  width: 100%;
  height: 60vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #3f0071;
}

.grid {
  height: 100vh;
}
@media screen and (max-width: 750px) {
  .grid {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
}

.wrapper {
  display: flex;
  height: 92vh;
  width: 100%;
}
.wrapper .data-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  width: 80vw;
  margin-top: 2rem;
}
.wrapper .data-box .header {
  display: flex;
  justify-content: space-between;
  background-color: #3f0071;
  border-radius: 5px;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  width: 90%;
}
.wrapper .data-box .header-title {
  color: #f5f5f5;
  font-weight: 400;
  padding: 1rem;
}
.wrapper .data-box .header .date-container {
  display: flex;
  align-items: center;
}
.wrapper .data-box .header .date-container #header-subtitle {
  color: #f5f5f5;
  font-size: small;
  font-weight: 300;
  margin-top: 0;
}
.wrapper .data-box .header .date-container .header-date {
  padding: 1rem;
  padding-left: 0.5rem;
  color: #f5f5f5;
  background-color: #3f0071;
  border: none;
  outline: none;
  border-radius: 5px;
}
.wrapper .data-box .header .date-container .header-date::-webkit-calendar-picker-indicator {
  filter: invert(1);
}
.wrapper .data-box .content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 1rem;
  width: 90%;
  height: 45%;
}
.wrapper .data-box .content .card {
  display: flex;
  flex-direction: column;
  width: 45%;
  height: 90%;
  background-color: white;
  border-radius: 5px;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}
.wrapper .data-box .content .card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #3f0071;
  border-radius: 5px 5px 0 0;
  padding: 0.5rem 1rem;
}
.wrapper .data-box .content .card-header .card-title {
  margin-top: 0;
  color: #f5f5f5;
}
.wrapper .data-box .content .card-content table {
  width: 100%;
  margin: 1rem 0;
  border-collapse: collapse;
}
.wrapper .data-box .content .card-content table tr {
  padding-right: 1rem;
  border-color: #fafafa;
}
.wrapper .data-box .content .card-content table tr:nth-child(odd) {
  background-color: #fafafa;
}
.wrapper .data-box .content .card-content table tr .parameter,
.wrapper .data-box .content .card-content table tr .goal,
.wrapper .data-box .content .card-content table tr .unit {
  color: #150050;
  font-size: 1rem;
}
.wrapper .data-box .content .card-content table tr .parameter {
  width: 60%;
  padding: 0.5rem 2.5rem;
}
.wrapper .data-box .content .card-content table tr .goal {
  width: 10%;
  padding-left: 1rem;
  text-align: end;
}
.wrapper .data-box .content .card-content table tr .unit {
  width: 20%;
  padding-left: 1rem;
}
.wrapper .data-box .content .card-content table tr .edit {
  width: 10%;
  padding: 0 1rem;
}
.wrapper .data-box .content .card-content .weekly-content {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem 4rem;
}
.wrapper .data-box .content .card-content .weekly-content .chart {
  display: flex;
  flex-direction: column;
}
.wrapper .data-box .content .card-content .weekly-content .chart-percentage {
  font-size: 0.7rem;
  margin-top: 0;
  color: #150050;
}
.wrapper .data-box .content .card-content .weekly-content .chart-bar {
  width: 1.5rem;
  height: 6rem;
  background-color: #fdd1e2;
  border-radius: 5px;
}
.wrapper .data-box .content .card-content .weekly-content .chart-bar .chart-fill {
  background-color: #f5f5f5;
  height: 60%;
  border-radius: 5px;
}
.wrapper .data-box .content .card-content .weekly-content .chart-date {
  font-size: 0.7rem;
  writing-mode: sideways-lr;
  text-orientation: sideways;
  color: #150050;
}
.wrapper .data-box .progress-content {
  width: 90%;
  height: 85%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding-bottom: 1rem;
  overflow-y: scroll;
}
.wrapper .data-box .progress-content .progress-card {
  width: 100%;
}
.wrapper .data-box .progress-content .progress-card .progress-card-header {
  background-color: #3f0071;
  border-radius: 5px 5px 0 0;
}
.wrapper .data-box .progress-content .progress-card .progress-card-header .progress-card-title {
  color: #f5f5f5;
  padding: 0.5rem 1rem;
  margin-top: 0;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body {
  display: flex;
  width: 100%;
  border-radius: 0 0 5px 5px;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.5rem;
  width: 80%;
  padding: 1rem;
  background-color: white;
  border-radius: 0 0 0 5px;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info {
  display: flex;
  align-items: center;
  gap: 4rem;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .box {
  display: flex;
  justify-content: space-between;
  gap: 0.5rem;
  width: 30%;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .box i {
  color: #3f0071;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .box p {
  margin-top: 0;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .box .flex-start {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 0.5rem;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .box .flex-end {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .progress-bar {
  min-width: 40%;
  height: 100%;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .progress-bar p {
  margin-top: 0;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .progress-bar .bar-total {
  background-color: #f5f5f5;
  width: 70%;
  height: 100%;
  border-radius: 5px;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .info .progress-bar .bar-total .bar-done {
  background-color: #fdd1e2;
  height: 100%;
  border-radius: 5px;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-info .progress-edit {
  color: #fb2576;
  align-self: flex-end;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-percent {
  background-color: #3f0071;
  width: 20%;
  border-radius: 0 0 5px 0;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0 2rem 1rem 2rem;
  padding-bottom: 1rem;
  min-height: fit-content;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-percent .percent-number {
  font-size: 4rem;
  color: #f5f5f5;
}
.wrapper .data-box .progress-content .progress-card .progress-card-body .progress-percent .percent-label {
  color: #f5f5f5;
  font-size: 1.5rem;
  font-weight: 100;
}

.empty {
  color: #150050;
  padding: 0.5rem 1.5rem;
}

/*# sourceMappingURL=styles.cs.map */
