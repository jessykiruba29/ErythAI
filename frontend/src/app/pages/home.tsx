import { useState } from "react";
import styles from "../styles/Home.module.css";

export default function Home(){
    const [query,setQuery]=useState("");
    const [file,setFile]=useState<File|null>(null);
    const [response,setResponse]=useState<any>(null);
    const [loading,setLoading]=useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    const formData = new FormData();
    formData.append("query", query);
    if (file) formData.append("file", file);

    const res = await fetch("http://localhost:8000/explain", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResponse(data);
    setLoading(false);
  };

  return (
    <main className={styles.container}>
      <h1 className={styles.title}>Eryth AI</h1>
      <p className={styles.subtitle}>
        Understand your blood report in plain words.
      </p>

      <form onSubmit={handleSubmit} className={styles.form}>
        <input
          type="text"
          placeholder="Search for a term in your report..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className={styles.input}
        />
        <input
          type="file"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className={styles.fileInput}
        />
        <button
          type="submit"
          disabled={loading}
          className={styles.button}
        >
          {loading ? "Thinking..." : "Explain"}
        </button>
      </form>

      {response && (
        <div className={styles.card}>
          <h2 className={styles.cardTitle}>{response.term}</h2>
          {response.value_in_report && (
            <p className={styles.value}>
              Value in report: {response.value_in_report}
            </p>
          )}
          <p className={styles.explanation}>{response.formatted_response}</p>
        </div>
      )}
    </main>
  );
}
