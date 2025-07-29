const canvas = document.getElementById('pongCanvas');
const ctx = canvas.getContext('2d');

// Game settings
const PADDLE_WIDTH = 10;
const PADDLE_HEIGHT = 100;
const BALL_SIZE = 16;
const PLAYER_X = 30;
const AI_X = canvas.width - PLAYER_X - PADDLE_WIDTH;
const PADDLE_SPEED = 6;
const AI_SPEED = 4;

// Game state
let playerY = canvas.height / 2 - PADDLE_HEIGHT / 2;
let aiY = playerY;
let ballX = canvas.width / 2 - BALL_SIZE / 2;
let ballY = canvas.height / 2 - BALL_SIZE / 2;
let ballSpeedX = 5 * (Math.random() < 0.5 ? 1 : -1);
let ballSpeedY = (Math.random() * 4 + 2) * (Math.random() < 0.5 ? 1 : -1);

let playerScore = 0;
let aiScore = 0;

// Mouse control
canvas.addEventListener('mousemove', (e) => {
  const rect = canvas.getBoundingClientRect();
  const mouseY = e.clientY - rect.top;
  playerY = mouseY - PADDLE_HEIGHT / 2;
  // Clamp paddle within bounds
  if (playerY < 0) playerY = 0;
  if (playerY > canvas.height - PADDLE_HEIGHT) playerY = canvas.height - PADDLE_HEIGHT;
});

function drawRect(x, y, w, h, color) {
  ctx.fillStyle = color;
  ctx.fillRect(x, y, w, h);
}

function drawCircle(x, y, r, color) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI * 2);
  ctx.closePath();
  ctx.fill();
}

function drawNet() {
  ctx.strokeStyle = "#555";
  ctx.setLineDash([10, 15]);
  ctx.beginPath();
  ctx.moveTo(canvas.width / 2, 0);
  ctx.lineTo(canvas.width / 2, canvas.height);
  ctx.stroke();
  ctx.setLineDash([]);
}

function drawScore() {
  ctx.font = "32px Arial";
  ctx.fillStyle = "#fff";
  ctx.fillText(playerScore, canvas.width / 4, 50);
  ctx.fillText(aiScore, canvas.width * 3 / 4, 50);
}

function resetBall() {
  ballX = canvas.width / 2 - BALL_SIZE / 2;
  ballY = canvas.height / 2 - BALL_SIZE / 2;
  ballSpeedX = 5 * (Math.random() < 0.5 ? 1 : -1);
  ballSpeedY = (Math.random() * 4 + 2) * (Math.random() < 0.5 ? 1 : -1);
}

function aiMove() {
  const aiCenter = aiY + PADDLE_HEIGHT / 2;
  if (aiCenter < ballY + BALL_SIZE / 2 - 10) {
    aiY += AI_SPEED;
  } else if (aiCenter > ballY + BALL_SIZE / 2 + 10) {
    aiY -= AI_SPEED;
  }
  // Clamp within bounds
  if (aiY < 0) aiY = 0;
  if (aiY > canvas.height - PADDLE_HEIGHT) aiY = canvas.height - PADDLE_HEIGHT;
}

function update() {
  // Move ball
  ballX += ballSpeedX;
  ballY += ballSpeedY;

  // Top and bottom wall collision
  if (ballY <= 0 || ballY + BALL_SIZE >= canvas.height) {
    ballSpeedY = -ballSpeedY;
    ballY = ballY <= 0 ? 0 : canvas.height - BALL_SIZE;
  }

  // Paddle collision: Player
  if (
    ballX <= PLAYER_X + PADDLE_WIDTH &&
    ballY + BALL_SIZE >= playerY &&
    ballY <= playerY + PADDLE_HEIGHT &&
    ballX > PLAYER_X
  ) {
    ballSpeedX = -ballSpeedX;
    // Add spin based on hit location
    let hitPos = (ballY + BALL_SIZE / 2) - (playerY + PADDLE_HEIGHT / 2);
    ballSpeedY = hitPos * 0.25;
    ballX = PLAYER_X + PADDLE_WIDTH; // Prevent sticking
  }

  // Paddle collision: AI
  if (
    ballX + BALL_SIZE >= AI_X &&
    ballY + BALL_SIZE >= aiY &&
    ballY <= aiY + PADDLE_HEIGHT &&
    ballX < AI_X + PADDLE_WIDTH
  ) {
    ballSpeedX = -ballSpeedX;
    let hitPos = (ballY + BALL_SIZE / 2) - (aiY + PADDLE_HEIGHT / 2);
    ballSpeedY = hitPos * 0.25;
    ballX = AI_X - BALL_SIZE; // Prevent sticking
  }

  // Score and reset
  if (ballX < 0) {
    aiScore++;
    resetBall();
  } else if (ballX > canvas.width) {
    playerScore++;
    resetBall();
  }

  aiMove();
}

function render() {
  // Clear
  drawRect(0, 0, canvas.width, canvas.height, '#000');
  drawNet();
  drawScore();

  // Draw paddles
  drawRect(PLAYER_X, playerY, PADDLE_WIDTH, PADDLE_HEIGHT, '#fff');
  drawRect(AI_X, aiY, PADDLE_WIDTH, PADDLE_HEIGHT, '#fff');

  // Draw ball
  drawCircle(ballX + BALL_SIZE / 2, ballY + BALL_SIZE / 2, BALL_SIZE / 2, "#fff");
}

function gameLoop() {
  update();
  render();
  requestAnimationFrame(gameLoop);
}

// Start the game
gameLoop();
