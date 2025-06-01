import React, { useState } from "react";
import axios from "axios";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [extractedSkills, setExtractedSkills] = useState([]);
  const [skillsInput, setSkillsInput] = useState("");
  const [matchedJobs, setMatchedJobs] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setResumeFile(e.target.files[0]);
  };

  const uploadResume = async () => {
    if (!resumeFile) {
      alert("Please select a PDF resume file.");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append("file", resumeFile);
    try {
      const response = await axios.post("http://localhost:8000/upload_resume/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setExtractedSkills(response.data.extracted_skills);
      setSkillsInput(response.data.extracted_skills.join(", "));
      setMatchedJobs([]);
    } catch (error) {
      alert("Error uploading resume: " + error.message);
    }
    setLoading(false);
  };

  const fetchRecommendations = async () => {
    if (!skillsInput.trim()) {
      alert("Please enter skills to match jobs.");
      return;
    }
    setLoading(true);
    const skillsArray = skillsInput.split(",").map((s) => s.trim());
    try {
      const response = await axios.post("http://localhost:8000/recommend_jobs/", skillsArray);
      setMatchedJobs(response.data.matched_jobs);
    } catch (error) {
      alert("Error fetching job recommendations: " + error.message);
    }
    setLoading(false);
  };

  return (
    <>
      <div className="content" style={{ backgroundColor: "black", minHeight: "100vh" }}>
        <nav className="navbar">
          <div className="navbar-left">
            <div className="logo">Advanced Tech Insights</div>
            <div className="college-name">Anantrao Pawar College Of Engineering &amp; Research.</div>
          </div>
          <ul className="nav-links">
            <li><a href="#home" className="active">Home</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
        <header className="hero">
          <div className="hero-text">
            <section className="about-section">
              <h2>About A.B.M.S. Parishad</h2>
              <p>
                Akhil Bharatiya Maratha Shikshan Parishad (A.B.M.S Parishad), an educational trust was founded by a team of renowned educationists and social reformers. It was established in 1907 with the thought “Bahujan Hitay, Bahujan Sukhaya”. In the first half of the 20th century A.B.M.S. Parishad made a commendable contribution of awakening and inspiring the masses who were deprived of education for generations. Owing to its inspiration, large number of educational institution were established throughout Maharashtra and outside Maharashtra. A.B.M.S Parishad draws its inspiration from Mahatma Phule, Rajashri Shahu Maharaj, the Ruler of Kolhapur and Dr. Babasaheb Ambedkar who fought for economic, social and political justice and advocated empowerment of economically and socially disadvantaged section of the society.
              </p>
            </section>
            <section className="about-section">
              <h2>About APCOER</h2>
              <p>
                Anantrao Pawar College of Engineering and Research is situated in nation’s education hub, Pune and recognized for its quality education and research. It is the institute of Akhil Bhartiya Maratha Shikshan Parishad, Parvati Pune 09, an educational trust was founded by a team of renowned educationists and social reformers. The institute is situated in the area of 10 acres of land surrounded by beautiful landscape of Sahyadri Hills of Western Ghat nearing to famous Parvati Hills. The institute is established in 2012 having 5 UG and 2 PG courses affiliated to SPPU, Pune. Institute is on creating versatile engineers who can apply their knowledge and skills in any field across the globe. Highly qualified faculty members, well equipped laboratories, extensive industry – academia interactions all serve to make engineering education at APCOER campus a unique and enriching experience.
              </p>
            </section>
            <p className="project-name">Studysync Career Opportunities</p>
          </div>
        </header>
        <main className="main-content">
          <section className="upload-section">
            <h3>Upload Resume (PDF)</h3>
            <input type="file" accept="application/pdf" onChange={handleFileChange} />
            <button onClick={uploadResume} disabled={loading}>
              {loading ? "Uploading..." : "Upload"}
            </button>
          </section>
          <section className="skills-section">
            <h3>Extracted Skills</h3>
            <textarea
              rows={3}
              value={skillsInput}
              onChange={(e) => setSkillsInput(e.target.value)}
              placeholder="Skills extracted from resume or enter manually, separated by commas"
            />
            <button onClick={fetchRecommendations} disabled={loading}>
              {loading ? "Fetching..." : "Get Job Recommendations"}
            </button>
          </section>
          <section className="jobs-section">
            <h3>Matched Jobs</h3>
            {matchedJobs.length === 0 && <p>No matched jobs to display.</p>}
            <div className="jobs-grid">
              {matchedJobs.map((job, index) => (
                <div key={index} className="job-card">
                  <a href={job.job_url} target="_blank" rel="noopener noreferrer">
                    <h4>{job.job_title}</h4>
                  </a>
                  <p>{job.company} - {job.location || "Remote"}</p>
                </div>
              ))}
            </div>
          </section>
        </main>
      </div>
    </>
  );
}

export default App;
