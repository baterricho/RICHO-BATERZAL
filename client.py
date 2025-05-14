<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta content="width=device-width, initial-scale=1" name="viewport" />
  <title>Barangay Tumbod e-Health Management System</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
    rel="stylesheet"
  />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter&display=swap"
    rel="stylesheet"
  />
  <style>
    body {
      font-family: "Inter", sans-serif;
      background: #f9fafb;
    }
    ul.scrollable {
      max-height: 220px;
      overflow-y: auto;
      padding-right: 0.5rem;
    }
    ul.scrollable::-webkit-scrollbar {
      width: 6px;
    }
    ul.scrollable::-webkit-scrollbar-thumb {
      background-color: #3b82f6;
      border-radius: 3px;
    }
    section {
      transition: opacity 0.3s ease;
    }
    section.hidden {
      opacity: 0;
      height: 0;
      overflow: hidden;
      pointer-events: none;
      position: absolute;
      width: 100%;
    }
    @media (min-width: 768px) {
      aside#sidebar {
        display: flex !important;
      }
    }
  </style>
</head>
<body>
  <div class="flex min-h-screen flex-col md:flex-row">
    <!-- Sidebar -->
    <aside
      class="bg-white w-full md:w-56 flex flex-row md:flex-col items-center md:items-start py-4 md:py-8 space-x-4 md:space-x-0 md:space-y-8 shadow-lg hidden md:flex"
      id="sidebar"
      aria-label="Sidebar Navigation"
    >
      <div class="flex items-center md:flex-col md:items-center space-x-3 md:space-x-0 md:space-y-2 px-4 md:px-0">
        <img
          alt="Barangay official seal with circular shape and colorful emblem"
          class="w-10 h-10 md:w-14 md:h-14"
          height="56"
          src="https://storage.googleapis.com/a1aa/image/1ab51a88-3dd4-4877-9fe5-463e73672faf.jpg"
          width="56"
        />
        <span class="text-lg font-semibold text-gray-800 hidden md:block">Dashboard</span>
      </div>
      <nav class="flex-1 w-full px-4 md:px-6 space-x-2 md:space-x-0 md:space-y-3 flex md:flex-col overflow-x-auto md:overflow-visible" role="navigation" aria-label="Main Navigation">
        <button
          class="w-full text-left text-gray-700 hover:bg-blue-600 hover:text-white rounded-md px-4 py-3 flex items-center space-x-3 font-medium transition whitespace-nowrap"
          id="addPatientBtn"
          type="button"
          aria-label="Add Patient"
        >
          <i class="fas fa-user-plus w-5"></i>
          <span>Add Patient</span>
        </button>
        <button
          class="w-full text-left text-gray-700 hover:bg-blue-600 hover:text-white rounded-md px-4 py-3 flex items-center space-x-3 font-medium transition whitespace-nowrap"
          id="scheduleAppointmentBtn"
          type="button"
          aria-label="Schedule Appointment"
        >
          <i class="fas fa-calendar-plus w-5"></i>
          <span>Schedule Appointment</span>
        </button>
        <button
          class="w-full text-left text-gray-700 hover:bg-blue-600 hover:text-white rounded-md px-4 py-3 flex items-center space-x-3 font-medium transition whitespace-nowrap"
          id="viewHealthRecordsBtn"
          type="button"
          aria-label="View Health Records"
        >
          <i class="fas fa-notes-medical w-5"></i>
          <span>View Health Records</span>
        </button>
        <button
          class="w-full text-left text-gray-700 hover:bg-blue-600 hover:text-white rounded-md px-4 py-3 flex items-center space-x-3 font-medium transition whitespace-nowrap"
          id="generateReportsBtn"
          type="button"
          aria-label="Generate Reports"
        >
          <i class="fas fa-chart-bar w-5"></i>
          <span>Generate Reports</span>
        </button>
        <button
          class="w-full text-left text-gray-700 hover:bg-blue-600 hover:text-white rounded-md px-4 py-3 flex items-center space-x-3 font-medium mt-6 transition whitespace-nowrap"
          id="adminBtn"
          type="button"
          aria-label="Admin"
        >
          <i class="fas fa-user-shield w-5"></i>
          <span>Admin</span>
        </button>
      </nav>
      <div class="w-full px-4 md:px-6 mt-auto">
        <button
          class="w-full text-left text-gray-700 hover:bg-red-600 hover:text-white rounded-md px-4 py-3 flex items-center space-x-3 font-medium transition whitespace-nowrap"
          id="logoutBtn"
          type="button"
          aria-label="Logout"
        >
          <i class="fas fa-sign-out-alt w-5"></i>
          <span>Logout</span>
        </button>
      </div>
    </aside>
    <!-- Main content -->
    <main class="flex-1 p-6 md:p-10 max-w-5xl mx-auto w-full">
      <h1
        class="text-3xl font-extrabold text-center text-gray-900 mb-1"
        id="pageTitle"
      >
        Barangay Tumbod e-Health Management System
      </h1>
      <p
        class="text-sm text-center text-gray-600 mb-8"
        id="pageSubtitle"
      >
        Dedicated to providing quality healthcare services through efficient digital management and community management.
      </p>

      <!-- Login Section -->
      <section
        class="max-w-md mx-auto bg-white rounded-xl shadow-lg p-8"
        id="loginSection"
        role="region"
        aria-label="Login Section"
      >
        <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Login</h2>
        <form id="loginForm" class="space-y-6" aria-describedby="loginDesc">
          <div>
            <label
              for="loginEmail"
              class="block text-sm font-medium text-gray-700 mb-2"
              >Email address</label
            >
            <input
              id="loginEmail"
              name="loginEmail"
              type="email"
              required
              placeholder="you@example.com"
              aria-required="true"
              aria-label="Email address"
              class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
            />
          </div>
          <div class="flex space-x-4">
            <button
              type="button"
              id="sendEmailLinkBtn"
              class="flex-1 bg-gray-700 hover:bg-gray-800 text-white font-semibold py-3 rounded-md transition flex items-center justify-center space-x-2"
              aria-label="Send Email Link"
            >
              <i class="fas fa-envelope"></i>
              <span>Send Email Link</span>
            </button>
            <button
              type="submit"
              id="loginWithEmailBtn"
              class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-md transition flex items-center justify-center space-x-2"
              aria-label="Login with Email"
            >
              <i class="fas fa-sign-in-alt"></i>
              <span>Login with Email</span>
            </button>
          </div>
        </form>
        <p class="mt-6 text-center text-gray-500 text-xs" id="loginDesc">
          Barangay Tumbod e-Health Management System
        </p>
      </section>

      <!-- Add New Patient Section -->
      <section
        class="max-w-3xl mx-auto mt-8 bg-white rounded-lg shadow p-6 hidden"
        id="addPatientSection"
        role="region"
        aria-label="Add New Patient Section"
      >
        <h2 class="text-xl font-bold mb-4 text-center text-gray-800">
          Add New Patient
        </h2>
        <form id="addPatientForm" class="space-y-4">
          <div>
            <label
              class="block text-sm font-medium mb-1 text-gray-700"
              for="patientName"
              >Patient Name</label
            >
            <input
              class="w-full border border-gray-400 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
              id="patientName"
              name="patientName"
              placeholder="Enter patient name"
              required
              type="text"
              aria-required="true"
            />
          </div>
          <button
            class="bg-blue-600 text-white px-4 py-2 rounded text-sm font-semibold hover:bg-blue-700 transition"
            type="submit"
            aria-label="Add Patient"
          >
            Add Patient
          </button>
        </form>
        <div
          class="mt-4 max-h-48 overflow-y-auto border border-gray-200 rounded p-3"
          tabindex="0"
          aria-live="polite"
          aria-atomic="true"
        >
          <h3 class="font-semibold mb-2 text-gray-700">Patients List:</h3>
          <ul class="list-disc list-inside text-sm text-gray-600 scrollable" id="patientList"></ul>
        </div>
      </section>

      <!-- Schedule Appointment Section -->
      <section
        class="max-w-3xl mx-auto mt-8 bg-white rounded-lg shadow p-6 hidden"
        id="scheduleAppointmentSection"
        role="region"
        aria-label="Schedule Appointment Section"
      >
        <h2 class="text-xl font-bold mb-4 text-center text-gray-800">
          Schedule Appointment
        </h2>
        <form id="scheduleAppointmentForm" class="space-y-4">
          <div>
            <label
              class="block text-sm font-medium mb-1 text-gray-700"
              for="appointmentPatient"
              >Patient Name</label
            >
            <select
              class="w-full border border-gray-400 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
              id="appointmentPatient"
              name="appointmentPatient"
              required
              aria-required="true"
            >
              <option value="" disabled selected>Select patient</option>
            </select>
          </div>
          <div>
            <label
              class="block text-sm font-medium mb-1 text-gray-700"
              for="appointmentDate"
              >Date</label
            >
            <input
              class="w-full border border-gray-400 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
              id="appointmentDate"
              name="appointmentDate"
              required
              type="date"
              aria-required="true"
            />
          </div>
          <button
            class="bg-blue-600 text-white px-4 py-2 rounded text-sm font-semibold hover:bg-blue-700 transition"
            type="submit"
            aria-label="Schedule Appointment"
          >
            Schedule
          </button>
        </form>
        <div
          class="mt-4 max-h-48 overflow-y-auto border border-gray-200 rounded p-3"
          tabindex="0"
          aria-live="polite"
          aria-atomic="true"
        >
          <h3 class="font-semibold mb-2 text-gray-700">Appointments List:</h3>
          <ul class="list-disc list-inside text-sm text-gray-600 scrollable" id="appointmentList"></ul>
        </div>
      </section>

      <!-- View Health Records Section -->
      <section
        class="max-w-3xl mx-auto mt-8 bg-white rounded-lg shadow p-6 hidden"
        id="viewHealthRecordsSection"
        role="region"
        aria-label="View Health Records Section"
      >
        <h2 class="text-xl font-bold mb-4 text-center text-gray-800">
          Health Records
        </h2>
        <ul
          class="list-disc list-inside text-sm text-gray-600 max-h-48 overflow-y-auto scrollable"
          id="healthRecordsList"
          tabindex="0"
          aria-live="polite"
          aria-atomic="true"
        ></ul>
      </section>

      <!-- Generate Reports Section -->
      <section
        class="max-w-3xl mx-auto mt-8 bg-white rounded-lg shadow p-6 hidden"
        id="generateReportsSection"
        role="region"
        aria-label="Generate Reports Section"
      >
        <h2 class="text-xl font-bold mb-4 text-center text-gray-800">Reports</h2>
        <div class="space-y-2 text-gray-700 text-sm">
          <p>Total Patients: <span id="reportTotalPatients">0</span></p>
          <p>Today's Appointments: <span id="reportTodaysAppointments">0</span></p>
        </div>
      </section>

      <!-- Admin Section -->
      <section
        class="max-w-3xl mx-auto mt-8 bg-white rounded-lg shadow p-6 hidden"
        id="adminSection"
        role="region"
        aria-label="Admin Section"
      >
        <h2 class="text-xl font-bold mb-4 text-center text-gray-800">
          Admins List
        </h2>
        <div
          class="max-h-48 overflow-y-auto border border-gray-200 rounded p-3"
          tabindex="0"
          aria-live="polite"
          aria-atomic="true"
        >
          <ul
            class="list-disc list-inside text-sm text-gray-600 scrollable"
            id="adminList"
          ></ul>
        </div>
      </section>
    </main>
  </div>

  <script>
    // Sidebar buttons and sections
    const sidebar = document.getElementById("sidebar");
    const addPatientBtn = document.getElementById("addPatientBtn");
    const scheduleAppointmentBtn = document.getElementById("scheduleAppointmentBtn");
    const viewHealthRecordsBtn = document.getElementById("viewHealthRecordsBtn");
    const generateReportsBtn = document.getElementById("generateReportsBtn");
    const adminBtn = document.getElementById("adminBtn");
    const logoutBtn = document.getElementById("logoutBtn");

    const addPatientSection = document.getElementById("addPatientSection");
    const scheduleAppointmentSection = document.getElementById("scheduleAppointmentSection");
    const viewHealthRecordsSection = document.getElementById("viewHealthRecordsSection");
    const generateReportsSection = document.getElementById("generateReportsSection");
    const adminSection = document.getElementById("adminSection");
    const loginSection = document.getElementById("loginSection");

    const pageTitle = document.getElementById("pageTitle");
    const pageSubtitle = document.getElementById("pageSubtitle");

    // Data storage
    let patients = [];
    let appointments = [];
    let admins = [];

    // Utility to hide all main sections except login
    function hideAllSections() {
      addPatientSection.classList.add("hidden");
      scheduleAppointmentSection.classList.add("hidden");
      viewHealthRecordsSection.classList.add("hidden");
      generateReportsSection.classList.add("hidden");
      adminSection.classList.add("hidden");
      loginSection.classList.add("hidden");
    }

    // Show login section and hide sidebar
    function showLogin() {
      hideAllSections();
      loginSection.classList.remove("hidden");
      sidebar.classList.add("hidden");
      pageTitle.textContent = "Barangay Tumbod e-Health Management System";
      pageSubtitle.textContent = "Please login with your email to continue.";
    }

    // Show dashboard sections (sidebar visible)
    function showDashboardSection(section, title, subtitle) {
      hideAllSections();
      section.classList.remove("hidden");
      sidebar.classList.remove("hidden");
      pageTitle.textContent = title;
      pageSubtitle.textContent = subtitle;
    }

    // Show Add Patient Section
    function showAddPatient() {
      showDashboardSection(addPatientSection, "Add New Patient", "Register a new patient.");
      updatePatientList();
    }

    // Show Schedule Appointment Section
    function showScheduleAppointment() {
      showDashboardSection(
        scheduleAppointmentSection,
        "Schedule Appointment",
        "Schedule an appointment for a patient."
      );
      updateAppointmentPatientOptions();
      updateAppointmentList();
    }

    // Show View Health Records Section
    function showViewHealthRecords() {
      showDashboardSection(viewHealthRecordsSection, "Health Records", "View all patient health records.");
      updateHealthRecordsList();
    }

    // Show Generate Reports Section
    function showGenerateReports() {
      showDashboardSection(generateReportsSection, "Reports", "Summary reports of the system.");
      updateReports();
    }

    // Show Admin Section
    function showAdmin() {
      showDashboardSection(adminSection, "Admins List", "Manage admin users for the system.");
      updateAdminList();
    }

    // Event listeners for sidebar buttons
    addPatientBtn.addEventListener("click", showAddPatient);
    scheduleAppointmentBtn.addEventListener("click", showScheduleAppointment);
    viewHealthRecordsBtn.addEventListener("click", showViewHealthRecords);
    generateReportsBtn.addEventListener("click", showGenerateReports);
    adminBtn.addEventListener("click", showAdmin);
    logoutBtn.addEventListener("click", () => {
      showLogin();
    });

    // Add Patient Form
    const addPatientForm = document.getElementById("addPatientForm");
    const patientList = document.getElementById("patientList");
    addPatientForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const patientNameInput = document.getElementById("patientName");
      const patientName = patientNameInput.value.trim();
      if (patientName && !patients.some((p) => p.toLowerCase() === patientName.toLowerCase())) {
        patients.push(patientName);
        updatePatientList();
        patientNameInput.value = "";
      } else if (patients.some((p) => p.toLowerCase() === patientName.toLowerCase())) {
        alert("Patient already exists.");
      }
    });
    function updatePatientList() {
      patientList.innerHTML = "";
      patients.forEach((patient) => {
        const li = document.createElement("li");
        li.textContent = patient;
        patientList.appendChild(li);
      });
    }

    // Schedule Appointment Form
    const scheduleAppointmentForm = document.getElementById("scheduleAppointmentForm");
    const appointmentPatientSelect = document.getElementById("appointmentPatient");
    const appointmentList = document.getElementById("appointmentList");
    scheduleAppointmentForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const patientName = appointmentPatientSelect.value;
      const appointmentDate = document.getElementById("appointmentDate").value;
      if (patientName && appointmentDate) {
        appointments.push({ patient: patientName, date: appointmentDate });
        updateAppointmentList();
        scheduleAppointmentForm.reset();
      }
    });
    function updateAppointmentPatientOptions() {
      appointmentPatientSelect.innerHTML = '<option value="" disabled selected>Select patient</option>';
      patients.forEach((patient) => {
        const option = document.createElement("option");
        option.value = patient;
        option.textContent = patient;
        appointmentPatientSelect.appendChild(option);
      });
    }
    function updateAppointmentList() {
      appointmentList.innerHTML = "";
      appointments.forEach((app) => {
        const li = document.createElement("li");
        li.textContent = `${app.patient} - ${new Date(app.date).toLocaleDateString()}`;
        appointmentList.appendChild(li);
      });
    }

    // View Health Records (list patients and their appointments)
    const healthRecordsList = document.getElementById("healthRecordsList");
    function updateHealthRecordsList() {
      healthRecordsList.innerHTML = "";
      if (patients.length === 0) {
        const li = document.createElement("li");
        li.textContent = "No patients registered.";
        healthRecordsList.appendChild(li);
        return;
      }
      patients.forEach((patient) => {
        const li = document.createElement("li");
        const patientAppointments = appointments.filter((a) => a.patient === patient);
        let apptText =
          patientAppointments.length > 0
            ? patientAppointments.map((a) => new Date(a.date).toLocaleDateString()).join(", ")
            : "No appointments";
        li.textContent = `${patient} - Appointments: ${apptText}`;
        healthRecordsList.appendChild(li);
      });
    }

    // Generate Reports
    const reportTotalPatients = document.getElementById("reportTotalPatients");
    const reportTodaysAppointments = document.getElementById("reportTodaysAppointments");
    function updateReports() {
      reportTotalPatients.textContent = patients.length;
      const today = new Date();
      const todaysAppts = appointments.filter((a) => {
        const d = new Date(a.date);
        return (
          d.getDate() === today.getDate() &&
          d.getMonth() === today.getMonth() &&
          d.getFullYear() === today.getFullYear()
        );
      });
      reportTodaysAppointments.textContent = todaysAppts.length;
    }

    // Admin List
    const adminList = document.getElementById("adminList");
    function updateAdminList() {
      adminList.innerHTML = "";
      admins.forEach((admin) => {
        const li = document.createElement("li");
        li.textContent = `${admin.name} (${admin.email})`;
        adminList.appendChild(li);
      });
    }

    // Login form and buttons
    const loginForm = document.getElementById("loginForm");
    const loginEmailInput = document.getElementById("loginEmail");
    const sendEmailLinkBtn = document.getElementById("sendEmailLinkBtn");

    // Simulate sending email link
    sendEmailLinkBtn.addEventListener("click", () => {
      const email = loginEmailInput.value.trim();
      if (email) {
        alert(`A login link has been sent to ${email}. (Simulation)`);
      } else {
        alert("Please enter your email.");
      }
    });

    // Login with email (simulate login and show dashboard)
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = loginEmailInput.value.trim();
      if (email) {
        // Record email in admins if not already present
        if (!admins.some((a) => a.email === email)) {
          admins.push({ name: "Logged-in User", email: email });
          updateAdminList();
        }
        alert(`Logged in as ${email}`);
        showAddPatient();
      } else {
        alert("Please enter your email.");
      }
    });

    // Initial view: show login
    showLogin();
  </script>
</body>
</html>
