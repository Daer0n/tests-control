import React from "react";
import { useNavigate } from "react-router-dom";
import "./exerciseEndPage.css";

const ExerciseEndPage = () => {
  const navigate = useNavigate();
  const path = window.location.pathname;
  const parts = path.split("/");
  const maxScore = parts[parts.length - 2];
  const score = parts[parts.length - 1];

  return (
    <div className="center-content">
      <div className="main-content">
        <div className="score">
          <div className="score-text">Congratulations! You’ve completed the level!</div>
          <div>
            <div>Score: {score}</div>
            <div>Max score: {maxScore}</div>
          </div>
        </div>

        <button className="back-to-main-page" onClick={() => navigate("/student/")}>
          Back to menu
        </button>
      </div>
    </div>
  );
};

export default ExerciseEndPage;