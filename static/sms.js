// Select elements
const textarea = document.querySelector("textarea");
const charCountDisplay = document.querySelector(".char-count");
const recipients = document.querySelectorAll(".recipient input[type='checkbox']");
const summaryRecipients = document.querySelector(".card:nth-of-type(3) p:nth-of-type(1)");
const summaryLength = document.querySelector(".card:nth-of-type(3) p:nth-of-type(2)");
const summaryLanguage = document.querySelector(".card:nth-of-type(3) p:nth-of-type(3)");

// Dropdowns
const languageSelect = document.querySelectorAll("select")[1]; // second select is language
const templateSelect = document.querySelectorAll("select")[0]; // first select is template

// Character + SMS count
textarea.addEventListener("input", () => {
  const message = textarea.value;
  const length = message.length;
  const smsCount = Math.ceil(length / 160) || 0;

  charCountDisplay.textContent = `Characters: ${length}/160 | SMS Count: ${smsCount}`;
  summaryLength.innerHTML = `<strong>Message Length:</strong> ${length} characters (${smsCount} SMS)`;
});

// Recipient selection
recipients.forEach(checkbox => {
  checkbox.addEventListener("change", () => {
    let selectedGroups = [];
    let totalRecipients = 0;

    document.querySelectorAll(".recipient input:checked").forEach(cb => {
      selectedGroups.push(cb.parentElement.textContent.trim());
      const count = parseInt(cb.closest(".recipient").querySelector(".badge").textContent);
      totalRecipients += count;
    });

    summaryRecipients.innerHTML = `<strong>Recipients:</strong> ${totalRecipients} (${selectedGroups.length} group(s) selected)`;
  });
});

// Language update
languageSelect.addEventListener("change", () => {
  summaryLanguage.innerHTML = `<strong>Language:</strong> ${languageSelect.value}`;
});

// Template selection autofills message
templateSelect.addEventListener("change", () => {
  if (templateSelect.value !== "Select a template or write custom message") {
    textarea.value = `📌 ${templateSelect.value} reminder.\nPlease attend your appointment on time.`;
    const event = new Event("input"); // trigger character count recalculation
    textarea.dispatchEvent(event);
  }
});

// (Optional) Send SMS Button action
const sendBtn = document.querySelector(".send-btn");
sendBtn.addEventListener("click", () => {
  alert("✅ SMS Reminder queued for sending!");
});
