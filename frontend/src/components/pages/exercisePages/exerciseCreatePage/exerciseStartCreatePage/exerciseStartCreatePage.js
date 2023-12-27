import React, { useState } from "react";
import api from "../../../../../api/api";
import "./exerciseStartCreatePage.css";
import { useNavigate } from "react-router-dom";

const ExerciseStartCreatePage = () => {
    const path = window.location.pathname;
    const parts = path.split("/");
    const theme = parts[parts.length - 2];
    const level = parts[parts.length - 1];
    const [numberOfExercise, setNumberOfExercise] = useState(0);
    const [theoryInput, setTheoryInput] = useState("");
    const [exerciseId, setExerciseId] = useState();
    const navigate = useNavigate();

    const handleTheoryInputChange = (event) => {
        setTheoryInput(event.target.value);
    };

    const handleCreateExercise = async () => {
        try {
            const responce = await api.post(
                `/teacher/exercise/${theoryInput}/${theme}/${level}`
            );
            navigate(`/teacher/exercise/create/${responce.data.id}/${numberOfExercise}`);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="main">
            <div className="content">
                <div className="content-number">
                    <div className="text">Number of exercises</div>
                    <div className="text counter">{numberOfExercise}</div>
                    <div className="buttons">
                        <button
                            className="buttons-counter"
                            onClick={() =>
                                setNumberOfExercise(
                                    (prevIndex) => prevIndex - 1
                                )
                            }
                        >
                            -
                        </button>
                        <button
                            className="buttons-counter"
                            onClick={() =>
                                setNumberOfExercise(
                                    (prevIndex) => prevIndex + 1
                                )
                            }
                        >
                            +
                        </button>
                    </div>
                </div>
                <div className="content-theory">
                    <div className="text">Theory</div>
                    <input
                        className="theory-input"
                        value={theoryInput}
                        onChange={handleTheoryInputChange}
                    />
                </div>
            </div>
            <button
                className="start-creating-button"
                onClick={handleCreateExercise}
            >
                Start creating
            </button>
        </div>
    );
};

export default ExerciseStartCreatePage;
