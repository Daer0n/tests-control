import React from "react";
import "./exerciseEndCreatePage.css";
import { useNavigate } from "react-router-dom";

const ExerciseEndCreatePage = () => {
    const navigate = useNavigate();

    return (
        <div className="end-create">
            <div className="text">Do you want to save exercise?</div>
            <div className="button-container">
                <button
                    className="exit-button"
                    onClick={() => navigate("/teacher/")}
                >
                    Exit
                </button>
                <button
                    className="create-button"
                    onClick={() => navigate("/teacher/")}
                >
                    Create
                </button>
            </div>
        </div>
    );
};

export default ExerciseEndCreatePage;
