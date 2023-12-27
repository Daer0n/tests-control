import React, { useEffect, useState } from "react";
import api from "../../../../../api/api";
import "./exerciseStartPage.css";
import { useNavigate } from "react-router-dom";
import Arrow from "../../../../../assets/images/Arrow.svg";

const ExerciseStartPage = () => {
    const navigate = useNavigate();
    const [exercise, setExercise] = useState(null);

    useEffect(() => {
        const fetchExercise = async () => {
            const exerciseId = window.location.pathname.split("/").pop();
            try {
                const response = await api.get(
                    `/student/exercise/${exerciseId}/`
                );
                setExercise(response.data);
                console.log(exercise.data.id);
            } catch (error) {
                console.error(error);
            }
        };

        fetchExercise();
    }, [window.location.pathname]);

    return (
        <div>
            <div className="text">Theme: {exercise?.theme}</div>
            <div className="text">Level: {exercise?.level}</div>
            <div className="theory-container">
                <div className="text theory">Theory: {exercise?.theory}</div>
            </div>
            <div className="start-exercise">
                <div className="text">Start Exercise</div>
                <div onClick={()=> navigate(`/student/exercise/complete/${exercise.id}`)}>
                    <img src={Arrow} alt="settings" />
                </div>
            </div>
        </div>
    );
};

export default ExerciseStartPage;
