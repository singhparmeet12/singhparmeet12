/**
 * Parmeet Singh — Profile Showcase Engine
 * Minimal, Fast, Zero-Dependency Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // --------------------------------------------------------------------------
  // Dynamic Typing Role Bar Animation
  // --------------------------------------------------------------------------
  const roles = [
    "Full Stack Web Developer",
    "Python & Django Specialist",
    "Scalable Web Systems Architect",
    "AI & Computer Vision Builder"
  ];

  const roleTextEl = document.getElementById('roleText');
  let roleIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typingSpeed = 90;

  function typeRole() {
    const currentRole = roles[roleIndex];

    if (isDeleting) {
      charIndex--;
      roleTextEl.textContent = currentRole.substring(0, charIndex);
      typingSpeed = 45;
    } else {
      charIndex++;
      roleTextEl.textContent = currentRole.substring(0, charIndex);
      typingSpeed = 90;
    }

    if (!isDeleting && charIndex === currentRole.length) {
      // Pause at full word
      isDeleting = true;
      typingSpeed = 2000;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      typingSpeed = 450;
    }

    setTimeout(typeRole, typingSpeed);
  }

  typeRole();

  // --------------------------------------------------------------------------
  // Subtle Mouse Glow Follower on Terminal Card
  // --------------------------------------------------------------------------
  const terminal = document.getElementById('terminalWindow');
  if (terminal && window.matchMedia('(hover: hover)').matches) {
    terminal.addEventListener('mousemove', (e) => {
      const rect = terminal.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -3;
      const rotateY = ((x - centerX) / centerX) * 3;

      terminal.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    terminal.addEventListener('mouseleave', () => {
      terminal.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
      terminal.style.transition = 'transform 0.4s ease';
    });

    terminal.addEventListener('mouseenter', () => {
      terminal.style.transition = 'none';
    });
  }
});
