const repoBase = "https://github.com/peter-adepoju/Intro-to-Python-Course";

const weeks = [
  { week: 1, unit: "1", title: "Foundations", days: ["Intro + types", "Variables", "Strings", "I/O + f-strings", "Branching"], status: "Available", keywords: "types variables strings input output f-strings branching foundations" },
  { week: 2, unit: "1", title: "Iteration", days: ["while loops", "for + range", "Nested loops", "Approximation", "Loop patterns"], status: "Planned", keywords: "loops while for range nested approximation iteration" },
  { week: 3, unit: "1", title: "Functions", days: ["Defining functions", "Parameters", "Return + scope", "Docstrings", "Practice"], status: "Planned", keywords: "functions parameters return scope docstrings" },
  { week: 4, unit: "1", title: "Recursion", days: ["Recursive thinking", "Base cases", "Call stack", "Fibonacci", "Mutual recursion"], status: "Planned", keywords: "recursion base cases call stack fibonacci" },
  { week: 5, unit: "2", title: "Tuples + Lists", days: ["Tuples", "Lists", "Mutation + alias", "List methods", "Iteration patterns"], status: "Planned", keywords: "tuples lists mutation alias methods" },
  { week: 6, unit: "2", title: "Dictionaries + Mutation", days: ["Dictionaries", "Dict methods", "Nested dicts", "Mutable vs immutable", "Comprehensions"], status: "Planned", keywords: "dictionaries mutation nested dicts comprehensions" },
  { week: 7, unit: "3", title: "Testing + Debugging", days: ["Error types", "try/except", "Assertions + tests", "Debugging strategies", "Code quality"], status: "Planned", keywords: "testing debugging errors exceptions assertions code quality" },
  { week: 8, unit: "midterm", title: "Midterm Review", days: ["Review Weeks 1–3", "Review Weeks 4–6", "Review Week 7", "Midterm exam", "Debrief"], status: "Planned", keywords: "midterm exam review" },
  { week: 9, unit: "4", title: "OOP I", days: ["What is OOP?", "Classes + __init__", "Methods + self", "Encapsulation", "Practice"], status: "Planned", keywords: "oop classes init methods self encapsulation" },
  { week: 10, unit: "4", title: "OOP II", days: ["Inheritance", "super()", "Polymorphism", "Class design", "OOP project"], status: "Planned", keywords: "inheritance super polymorphism class design project" },
  { week: 11, unit: "5", title: "Complexity", days: ["Why complexity?", "Big-O", "Best/avg/worst", "Common classes", "Analysis practice"], status: "Planned", keywords: "complexity big-o analysis runtime" },
  { week: 12, unit: "5", title: "Searching + Sorting", days: ["Linear search", "Binary search", "Bubble sort", "Merge sort", "Quick sort"], status: "Planned", keywords: "searching sorting linear binary bubble merge quick" },
  { week: 13, unit: "6", title: "Data + Modules", days: ["Modules + import", "File I/O", "String parsing", "Data analysis", "Visualization intro"], status: "Planned", keywords: "modules file io parsing data analysis visualization" },
  { week: 14, unit: "6", title: "Capstone", days: ["Final project", "Final project", "Final project", "Final exam", "Course synthesis"], status: "Planned", keywords: "capstone final project exam synthesis" }
];

const quizQuestions = [
  {
    question: "Which Python type is best for storing text?",
    answers: ["int", "str", "float", "bool"],
    correct: 1,
    explain: "Text is stored using the string type, written as str."
  },
  {
    question: "What does this expression produce: 7 // 2?",
    answers: ["3.5", "3", "4", "Error"],
    correct: 1,
    explain: "// is floor division, so 7 // 2 evaluates to 3."
  },
  {
    question: "Which statement is used for decision-making?",
    answers: ["import", "def", "if", "print"],
    correct: 2,
    explain: "if statements allow a program to branch based on a condition."
  },
  {
    question: "Which line creates a variable named score?",
    answers: ["score == 10", "score = 10", "int(score)", "print(score)"],
    correct: 1,
    explain: "A single equals sign assigns a value to a variable."
  },
  {
    question: "What does an f-string help you do?",
    answers: ["Format strings with variables", "Find files", "Create functions", "Force integer division"],
    correct: 0,
    explain: "f-strings let you place expressions inside strings using braces."
  }
];

const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");
navToggle?.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", open ? "true" : "false");
});

function getProgressKey(week) { return `intro-python-week-${week}`; }
function isWeekComplete(week) { return localStorage.getItem(getProgressKey(week)) === "true"; }
function setWeekComplete(week, complete) { localStorage.setItem(getProgressKey(week), complete ? "true" : "false"); }

function renderWeeks() {
  const search = document.querySelector("#course-search")?.value.trim().toLowerCase() || "";
  const filter = document.querySelector("#unit-filter")?.value || "all";
  const container = document.querySelector("#course-cards");
  if (!container) return;

  const filtered = weeks.filter(item => {
    const matchesFilter = filter === "all" || item.unit === filter;
    const text = `${item.week} ${item.title} ${item.days.join(" ")} ${item.keywords}`.toLowerCase();
    return matchesFilter && text.includes(search);
  });

  container.innerHTML = filtered.map(item => {
    const complete = isWeekComplete(item.week);
    const dayTags = item.days.map(day => `<span class="tag">${day}</span>`).join("");
    const weekLink = item.week === 1
      ? `<a class="button small secondary" href="${repoBase}/tree/main/Week_01" target="_blank" rel="noreferrer">Open materials</a>`
      : `<span class="tag">Coming soon</span>`;
    return `
      <article class="week-card ${complete ? "complete" : ""}">
        <div class="week-card-header">
          <div>
            <p class="eyebrow">Week ${item.week} • Unit ${item.unit}</p>
            <h3>${item.title}</h3>
          </div>
          <span class="tag">${item.status}</span>
        </div>
        <p>${item.days.join(" • ")}</p>
        <div class="tags">${dayTags}</div>
        <div>${weekLink}</div>
        <label class="progress-check">
          <input type="checkbox" data-week="${item.week}" ${complete ? "checked" : ""} />
          Mark week as complete
        </label>
      </article>
    `;
  }).join("") || `<p>No weeks matched your search.</p>`;

  container.querySelectorAll("input[type='checkbox'][data-week]").forEach(box => {
    box.addEventListener("change", event => {
      const week = Number(event.target.dataset.week);
      setWeekComplete(week, event.target.checked);
      renderWeeks();
      updateProgress();
    });
  });
}

function updateProgress() {
  const completed = weeks.filter(w => isWeekComplete(w.week)).length;
  const count = document.querySelector("#completed-count");
  const bar = document.querySelector("#progress-bar");
  if (count) count.textContent = completed;
  if (bar) bar.style.width = `${(completed / weeks.length) * 100}%`;
}

document.querySelector("#course-search")?.addEventListener("input", renderWeeks);
document.querySelector("#unit-filter")?.addEventListener("change", renderWeeks);

function renderQuiz() {
  const box = document.querySelector("#quiz-box");
  if (!box) return;
  box.innerHTML = quizQuestions.map((q, index) => `
    <div class="question" data-question="${index}">
      <h3>${index + 1}. ${q.question}</h3>
      <div class="answers">
        ${q.answers.map((answer, answerIndex) => `
          <label>
            <input type="radio" name="question-${index}" value="${answerIndex}" />
            <span>${answer}</span>
          </label>
        `).join("")}
      </div>
      <div class="feedback" aria-live="polite"></div>
    </div>
  `).join("");
}

function checkQuiz() {
  let score = 0;
  quizQuestions.forEach((q, index) => {
    const chosen = document.querySelector(`input[name="question-${index}"]:checked`);
    const feedback = document.querySelector(`.question[data-question="${index}"] .feedback`);
    if (!feedback) return;
    if (!chosen) {
      feedback.textContent = "Choose an answer.";
      feedback.className = "feedback wrong";
      return;
    }
    const isCorrect = Number(chosen.value) === q.correct;
    if (isCorrect) score += 1;
    feedback.textContent = `${isCorrect ? "Correct." : "Not quite."} ${q.explain}`;
    feedback.className = `feedback ${isCorrect ? "correct" : "wrong"}`;
  });
  const result = document.querySelector("#quiz-result");
  if (result) result.textContent = `Score: ${score}/${quizQuestions.length}`;
  localStorage.setItem("intro-python-quiz-score", String(score));
}

function resetQuiz() {
  renderQuiz();
  const result = document.querySelector("#quiz-result");
  if (result) result.textContent = "";
  localStorage.removeItem("intro-python-quiz-score");
}

document.querySelector("#submit-quiz")?.addEventListener("click", checkQuiz);
document.querySelector("#reset-quiz")?.addEventListener("click", resetQuiz);

const defaultCode = document.querySelector("#code-editor")?.value || "";
let pyodide = null;

async function loadPython() {
  const status = document.querySelector("#py-status");
  const output = document.querySelector("#output");
  const runButton = document.querySelector("#run-code");
  const loadButton = document.querySelector("#load-python");
  if (pyodide) return;
  if (status) status.textContent = "Loading Python runtime...";
  if (loadButton) loadButton.disabled = true;
  try {
    if (!window.loadPyodide) {
      await new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = "https://cdn.jsdelivr.net/pyodide/v314.0.1/full/pyodide.js";
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
      });
    }
    pyodide = await loadPyodide();
    if (status) status.textContent = "Python is ready.";
    if (output) output.textContent = "Python loaded successfully. You can run code now.";
    if (runButton) runButton.disabled = false;
  } catch (error) {
    if (status) status.textContent = "Could not load Python.";
    if (output) output.textContent = String(error);
    if (loadButton) loadButton.disabled = false;
  }
}

async function runCode() {
  const code = document.querySelector("#code-editor")?.value || "";
  const output = document.querySelector("#output");
  if (!pyodide) {
    if (output) output.textContent = "Load Python first.";
    return;
  }
  try {
    pyodide.runPython(`
import sys, io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
`);
    const result = await pyodide.runPythonAsync(code);
    const stdout = pyodide.runPython("sys.stdout.getvalue()");
    const stderr = pyodide.runPython("sys.stderr.getvalue()");
    const resultText = result === undefined ? "" : `\n${String(result)}`;
    if (output) output.textContent = `${stdout}${stderr}${resultText}`.trim() || "Code ran with no output.";
  } catch (error) {
    if (output) output.textContent = String(error);
  }
}

document.querySelector("#load-python")?.addEventListener("click", loadPython);
document.querySelector("#run-code")?.addEventListener("click", runCode);
document.querySelector("#reset-code")?.addEventListener("click", () => {
  const editor = document.querySelector("#code-editor");
  if (editor) editor.value = defaultCode;
});

const notesArea = document.querySelector("#notes-area");
const notesStatus = document.querySelector("#notes-status");
if (notesArea) {
  notesArea.value = localStorage.getItem("intro-python-notes") || "";
  notesArea.addEventListener("input", () => {
    localStorage.setItem("intro-python-notes", notesArea.value);
    if (notesStatus) notesStatus.textContent = "Saved.";
    window.clearTimeout(window.notesTimer);
    window.notesTimer = window.setTimeout(() => {
      if (notesStatus) notesStatus.textContent = "";
    }, 1200);
  });
}
document.querySelector("#clear-notes")?.addEventListener("click", () => {
  if (notesArea) notesArea.value = "";
  localStorage.removeItem("intro-python-notes");
  if (notesStatus) notesStatus.textContent = "Notes cleared.";
});

renderWeeks();
updateProgress();
renderQuiz();
