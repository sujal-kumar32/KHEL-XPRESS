// Modal Logic
const modal = document.querySelector(".post-modal");
const closeBtn = document.querySelector(".close-btn");
const textareaTrigger = document.querySelector(".user-input input");
const photoIcon = document.querySelectorAll(".action-btn")[1];

function showModal() {
  modal.classList.remove("hidden");
}

function hideModal() {
  modal.classList.add("hidden");
  clearPostModal(); // Also clear the content when modal closes
}

textareaTrigger.addEventListener("click", showModal);
photoIcon.addEventListener("click", showModal);
closeBtn.addEventListener("click", hideModal);

// Post Textarea + Upload Logic
const postText = document.getElementById("postText");
const postBtn = document.getElementById("postBtn");
const fileInput = document.getElementById("fileInput");
const previewImage = document.getElementById("previewImage");
const removeImage = document.getElementById("removeImage");

function updatePostButton() {
  postBtn.disabled = !(postText.value.trim() || fileInput.files.length > 0);
}

postText.addEventListener("input", updatePostButton);

fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      previewImage.src = reader.result;
      previewImage.style.display = "block";
      removeImage.style.display = "block";
      updatePostButton();
    };
    reader.readAsDataURL(file);
  }
});

removeImage.addEventListener("click", () => {
  fileInput.value = "";
  previewImage.src = "";
  previewImage.style.display = "none";
  removeImage.style.display = "none";
  updatePostButton();
});

function clearPostModal() {
  postText.value = "";
  fileInput.value = "";
  previewImage.src = "";
  previewImage.style.display = "none";
  removeImage.style.display = "none";
  postBtn.disabled = true;
}

// Emoji Picker Setup
const emojiBtn = document.querySelector("#emojiBtn");
const picker = new EmojiButton({
  position: "top-end",
  zIndex: 9999,
});

picker.on("emoji", (emoji) => {
  postText.value += emoji;
  updatePostButton();
});

emojiBtn.addEventListener("click", () => {
  picker.togglePicker(emojiBtn);
});

// Automatically submit the form when a file is selected
document.getElementById("coverInput").addEventListener("change", function () {
  document.querySelector("form").submit();
});

document.getElementById("profileInput").addEventListener("change", function () {
  document.querySelector("form").submit();
});
