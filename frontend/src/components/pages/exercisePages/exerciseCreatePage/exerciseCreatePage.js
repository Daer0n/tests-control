import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../../../api/api";
import "./exerciseCreatePage.css";

const ExerciseCreatePage = () => {
    const navigate = useNavigate();
    const path = window.location.pathname;
    const parts = path.split("/");
    const exerciseId = parts[parts.length - 2];
    const amountOfQuestions = parts[parts.length - 1];
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(1);
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [taskInputValue, setTaskInputValue] = useState("");
    const [answerInputValues, setAnswerInputValues] = useState([
        "",
        "",
        "",
        "",
    ]);

    const handleTaskInputChange = (event) => {
        setTaskInputValue(event.target.value);
    };

    const handleAnswerInputChange = (event, index) => {
        const newInputValues = [...answerInputValues];
        newInputValues[index] = event.target.value;
        setAnswerInputValues(newInputValues);
    };

    const handleRadioChange = (event) => {
        setSelectedAnswer(event.target.value);
    };

    const handleCreateQuestion = async () => {
        try {
            let questionText = taskInputValue.replace(/ /g, "_");
            const response = await api.post(
                `/teacher/question/${taskInputValue}/${exerciseId}/`
            );

            for (let i = 0; i < 4; i++) {
                let text = answerInputValues[i].replace(/ /g, "_");
                const isCorrect = i === selectedAnswer ? true : false;
                await api.post(
                    `teacher/answer/${text}/${isCorrect}/${response.data.id}/`
                );
            }

            if (currentQuestionIndex == amountOfQuestions) {
                navigate("/teacher/exercise/end");
            } else {
                setCurrentQuestionIndex(currentQuestionIndex + 1);
                setSelectedAnswer(null);
                setTaskInputValue("");
                setAnswerInputValues(["", "", "", ""]);
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="main-content">
            <div className="question">
                <div className="text">Question {currentQuestionIndex}</div>
            </div>
            <div className="content-wrapper">
                <div className="task-content">
                    <div className="text">Task</div>
                    <input
                        className="task-input"
                        value={taskInputValue}
                        onChange={handleTaskInputChange}
                    />
                </div>
                <div className="answer-content">
                    <div className="answers-content">
                        <div className="answer">
                            <input
                                type="radio"
                                className="answer-radio"
                                name="answer"
                                value="1"
                                checked={selectedAnswer === "1"}
                                onChange={handleRadioChange}
                            />
                            <input
                                className="write-answer"
                                value={answerInputValues[0]}
                                onChange={(event) =>
                                    handleAnswerInputChange(event, 0)
                                }
                            />
                        </div>
                        <div className="answer">
                            <input
                                type="radio"
                                name="answer"
                                value="2"
                                className="answer-radio"
                                checked={selectedAnswer === "2"}
                                onChange={handleRadioChange}
                            />
                            <input
                                className="write-answer"
                                value={answerInputValues[1]}
                                onChange={(event) =>
                                    handleAnswerInputChange(event, 1)
                                }
                            />
                        </div>
                        <div className="answer">
                            <input
                                type="radio"
                                name="answer"
                                value="3"
                                className="answer-radio"
                                checked={selectedAnswer === "3"}
                                onChange={handleRadioChange}
                            />
                            <input
                                className="write-answer"
                                value={answerInputValues[2]}
                                onChange={(event) =>
                                    handleAnswerInputChange(event, 2)
                                }
                            />
                        </div>
                        <div className="answer">
                            <input
                                type="radio"
                                name="answer"
                                value="4"
                                className="answer-radio"
                                checked={selectedAnswer === "4"}
                                onChange={handleRadioChange}
                            />
                            <input
                                className="write-answer"
                                value={answerInputValues[3]}
                                onChange={(event) =>
                                    handleAnswerInputChange(event, 3)
                                }
                            />
                        </div>
                    </div>
                </div>
            </div>
            <button onClick={handleCreateQuestion}>Create</button>
        </div>
    );
};

export default ExerciseCreatePage;
