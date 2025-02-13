import React, { useState } from "react";

const NewsFetcher = () => {
  const [topic, setTopic] = useState("");
  const [news, setNews] = useState([]);

  const fetchNews = async () => {
    const response = await fetch(`http://127.0.0.1:8000/news/?topic=${topic}`);
    const data = await response.json();
    setNews(data.news || []);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI News Curator</h2>
      <input
        type="text"
        placeholder="Enter topic (e.g., astronomy)"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <button onClick={fetchNews}>Fetch News</button>

      <div>
        {news.map((article, index) => (
          <div key={index} style={{ margin: "10px 0", borderBottom: "1px solid #ccc" }}>
            <h3>{article.title}</h3>
            <p>{article.summary}</p>
            <a href={article.url} target="_blank" rel="noopener noreferrer">Read More</a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NewsFetcher;