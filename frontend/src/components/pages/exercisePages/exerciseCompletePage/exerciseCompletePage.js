import React, { useState, useEffect } from "react";
import api from "../../../../api/api";
import "./exerciseCompletePage.css";
import { useNavigate } from "react-router-dom";

const ExerciseCompletePage = () => {
  const navigate = useNavigate();
  const [questions, setQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [initialQuestionIndex, setInitialQuestionIndex] = useState(0); // Новое состояние
  const [answers, setAnswers] = useState([]);
  const [selectedAnswer, setSelectedAnswer] = useState("");
  const [numberOfQuestions, setNumberOfQuestions] = useState(0);
  const [numberOfRightQuestions, setNumberOfRightQuestions] = useState(0);

  useEffect(() => {
    const fetchExercise = async () => {
      const exerciseId = window.location.pathname.split("/").pop();
      try {
        const response = await api.get(`/student/${exerciseId}/questions/`);
        setQuestions(response.data);
        setInitialQuestionIndex(response.data[0].id); // Установка значения initialQuestionIndex
        setNumberOfQuestions(0);
        setNumberOfRightQuestions(0);
      } catch (error) {
        console.error(error);
      }
    };

    fetchExercise();
  }, [window.location.pathname]);

  useEffect(() => {
    if (questions && questions.length > 0) {
      handleGetAnswers();
      setSelectedAnswer("");
    }
  }, [questions, currentQuestionIndex]);

  useEffect(() => {
    if (numberOfQuestions === questions.length && numberOfQuestions > 0) {
      navigate(
        `/student/exercise/end/${numberOfQuestions}/${numberOfRightQuestions}`
      );
    }
  }, [numberOfQuestions, numberOfRightQuestions, navigate, questions.length]);

  const handleAnswerSubmit = async () => {
    const response = await api.get(
      `/student/exercise/question/${initialQuestionIndex}/right-answer/`
    );
    console.log(selectedAnswer)
    console.log(response.data.text)
    if (selectedAnswer == response.data.text) {
      setNumberOfRightQuestions((prevCount) => prevCount + 1);
    }
    setInitialQuestionIndex((prevCount) => prevCount + 1)
    setNumberOfQuestions((prevCount) => prevCount + 1);
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex((prevIndex) => prevIndex + 1);
    }
  };

  const handleGetAnswers = async () => {
    try {
      const response = await api.get(
        `/student/exercise/question/${initialQuestionIndex}/answers/`
      );
      setAnswers(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const handleSelectAnswer = (event) => {
    setSelectedAnswer(event.target.value);
  };

  return (
    <div>
      {questions && questions.length > 0 && (
        <div>
          <div className="question-text">
            {questions[currentQuestionIndex]?.question_text}
          </div>
          {answers && answers.length > 0 && (
            <div>
              {answers.map((answer, index) => (
                <div key={index}>
                  <input
                    type="radio"
                    id={`answer-${index}`}
                    name="answer"
                    className="answer"
                    value={answer.text}
                    checked={selectedAnswer === answer.text}
                    onChange={handleSelectAnswer}
                  />
                  <label htmlFor={`answer-${index}`}>{answer.text}</label>
                </div>
              ))}
            </div>
          )}
          <button className="submit-answer" onClick={handleAnswerSubmit}>
            Submit
          </button>
        </div>
      )}
    </div>
  );
};

export default ExerciseCompletePage;