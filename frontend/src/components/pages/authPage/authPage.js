import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./authPage.css";
import api from "../../../api/api";

const Auth = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState("Username");
    const [password, setPassword] = useState("Password");
    const [loginError, setLoginError] = useState(false);
    const [passwordError, setPasswordError] = useState(false);

    const handleAuth = async () => {
        try {
            const response = await api.post(
                `/auth/login/${username}/${password}/`
            );
            const userRole = response.data.role;
            if (userRole === "Teacher") {
                navigate("/teacher/");
            } else if (userRole === "Student") {
                navigate("/student/");
            }
        } catch (error) {
            setLoginError(true);
            setPasswordError(true);
            console.error("Authentication failed", error);
            alert("Authentication failed");
        }
    };

    const handleUsernameClick = () => {
        setUsername("");
        setLoginError(false);
    };

    const handleUsernameBlur = () => {
        if (username === "") {
            setUsername("Username");
        }
    };

    const handlePasswordClick = () => {
        setPassword("");
        setPasswordError(false);
    };

    const handlePasswordBlur = () => {
        if (password === "") {
            setPassword("Password");
        }
    };

    return (
        <div className="app">
            <div className="app-name">Teacher&Kids.by</div>
            <div className="input-text">Login</div>
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                onClick={handleUsernameClick}
                onBlur={handleUsernameBlur}
                className={`input ${loginError ? "error" : ""}`}
            />
            <div className="input-text">Password</div>
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                onClick={handlePasswordClick}
                onBlur={handlePasswordBlur}
                className={`input ${passwordError ? "error" : ""}`}
            />
            <button className="start-button" onClick={handleAuth}>
                Start
            </button>
        </div>
    );
};

export default Auth;
