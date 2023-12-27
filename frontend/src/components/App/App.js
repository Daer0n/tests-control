import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import { useTheme } from "../../hooks/useTheme";
import Auth from "../pages/authPage/authPage";
import TeacherPage from "../pages/teacherPage/teacherPage";
import StudentPage from "../pages/studentPage/studentPage";
import Settings from "../pages/settingsPage/settingsPage";
import ExerciseStartPage from "../pages/exercisePages/exerciseCompletePage/exerciseStartPage/exerciseStartPage";
import ExerciseCompletePage from "../pages/exercisePages/exerciseCompletePage/exerciseCompletePage";
import ExerciseEndPage from "../pages/exercisePages/exerciseCompletePage/exerciseEndPage/exerciseEndPage";
import ExerciseStartCreatePage from "../pages/exercisePages/exerciseCreatePage/exerciseStartCreatePage/exerciseStartCreatePage";
import ExerciseCreatePage from "../pages/exercisePages/exerciseCreatePage/exerciseCreatePage";
import ExerciseEndCreatePage from "../pages/exercisePages/exerciseCreatePage/exerciseEndCreatePage/exerciseEndCreatePage";

function App() {
  const { theme, setTheme } = useTheme();

  React.useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
  }, [theme]);

  return (
    <div className="app">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Auth />} />
          <Route path="/teacher/" element={<TeacherPage />} />
          <Route path="/student/" element={<StudentPage />} />
          <Route path="/settings/" element={<Settings />} />
          <Route path="/student/exercise/start/:exerciseId" element={<ExerciseStartPage />} />
          <Route path="/student/exercise/complete/:exerciseId" element={<ExerciseCompletePage />} />
          <Route path="/student/exercise/end/:amountOfQuestion/:amountOfRightQuestion" element={<ExerciseEndPage />} />
          <Route path="/teacher/exercise/start/:theme/:level" element={<ExerciseStartCreatePage />} />
          <Route path="/teacher/exercise/create/:exerciseId/:amountOfQuestions" element={<ExerciseCreatePage />} />
          <Route path="/teacher/exercise/end" element={<ExerciseEndCreatePage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;