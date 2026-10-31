// Deliberate null/undefined property dereference fixture for Ada verification
function weaveJacquardPattern() {
  const engineState = null;
  console.log("Weaving pattern row:", engineState.spindleSpeed);
}

weaveJacquardPattern();
