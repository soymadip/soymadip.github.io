import { useState, useEffect } from "react";
import { createPortal } from "react-dom";
import CodeBlock from "@theme/CodeBlock";
import useBaseUrl from "@docusaurus/useBaseUrl";
import styles from "./styles.module.css";

// Required CSS for text selection and links inside PDFs
import "react-pdf/dist/Page/AnnotationLayer.css";
import "react-pdf/dist/Page/TextLayer.css";

// We'll load these only on the client to prevent SSR crashes
let Document, Page, pdfjs;

export default function SourcePreview({ path, label, sources }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);
  const [fileContents, setFileContents] = useState({});
  const [errors, setErrors] = useState({});
  const [mounted, setMounted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [isClient, setIsClient] = useState(false);

  // PDF specific states
  const [numPages, setNumPages] = useState(null);

  const sourceList = sources || [{ path, label }];

  useEffect(() => {
    setMounted(true);
    setIsClient(true);
    // Dynamically load react-pdf only in browser
    import("react-pdf").then((mod) => {
      Document = mod.Document;
      Page = mod.Page;
      pdfjs = mod.pdfjs;
      pdfjs.GlobalWorkerOptions.workerSrc = `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;
    });
    return () => setMounted(false);
  }, []);

  if (typeof window === "undefined") {
    const fs = eval('require("fs")');
    const nodePath = eval('require("path")');
    sourceList.forEach((src) => {
      if (!src.path) return;
      const diskPath = nodePath.join(process.cwd(), "static", src.path);
      if (!fs.existsSync(diskPath)) {
        console.error(`\x1b[31m[SourcePreview Error]\x1b[0m Source file not found: ${src.path}`);
      }
    });
  }

  useEffect(() => {
    setMounted(true);
    return () => setMounted(false);
  }, []);

  const currentFile = sourceList[activeIndex] || sourceList[0];
  const fullUrl = useBaseUrl(currentFile.path);
  const extension = currentFile.path.split(".").pop().toLowerCase();
  const isPDF = extension === "pdf";
  const imageExtensions = ["png", "jpg", "jpeg", "gif", "webp", "svg", "avif"];
  const isImage = imageExtensions.includes(extension);

  const fetchFile = (index) => {
    const file = sourceList[index];
    const fileExt = file.path.split(".").pop().toLowerCase();
    const isBinary = fileExt === "pdf" || imageExtensions.includes(fileExt);
    if (!file || fileContents[index] || isBinary) return;

    setLoading(true);
    fetch(file.path)
      .then((res) => {
        if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
        return res.text();
      })
      .then((text) => setFileContents((prev) => ({ ...prev, [index]: text })))
      .catch((err) => setErrors((prev) => ({ ...prev, [index]: err.message })))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    if (isOpen) {
      fetchFile(activeIndex);
      if (isPDF) {
        setNumPages(null);
      }
    }
  }, [isOpen, activeIndex, isPDF]);

  useEffect(() => {
    const handleEsc = (event) => {
      if (event.keyCode === 27) setIsOpen(false);
    };
    if (isOpen) {
      window.addEventListener("keydown", handleEsc);
      document.body.style.overflow = "hidden";
    }
    return () => {
      window.removeEventListener("keydown", handleEsc);
      document.body.style.overflow = "unset";
    };
  }, [isOpen]);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
    setLoading(false);
  }

  function onDocumentLoadError(error) {
    setErrors((prev) => ({ ...prev, [activeIndex]: error.message }));
    setLoading(false);
  }

  const modalElement =
    isOpen && mounted ? (
      <div className={styles.modalOverlay} onClick={() => setIsOpen(false)}>
        <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
          <div className={styles.modalHeader}>
            <h4 className={styles.modalTitle}>Source Preview</h4>
            <button className={styles.closeButton} onClick={() => setIsOpen(false)}>
              &times;
            </button>
          </div>

          {sourceList.length > 1 && (
            <div className={styles.tabs}>
              {sourceList.map((src, idx) => (
                <button
                  key={idx}
                  className={`${styles.tab} ${activeIndex === idx ? styles.activeTab : ""}`}
                  onClick={() => setActiveIndex(idx)}
                >
                  {src.label}
                </button>
              ))}
            </div>
          )}

          <div className={styles.modalBody}>
            {loading && !isPDF && <div className={styles.loading}>Loading...</div>}

            {errors[activeIndex] ? (
              <div className="admonition admonition-danger">
                <div className="admonition-heading">
                  <h5>File Not Found</h5>
                </div>
                <div className="admonition-content">
                  <p>The source file could not be loaded: <code>{currentFile.path}</code></p>
                  <p><em>Error: {errors[activeIndex]}</em></p>
                </div>
              </div>
            ) : (isPDF && Document) ? (
              <div className={styles.pdfViewer}>
                <Document
                  file={fullUrl}
                  onLoadSuccess={onDocumentLoadSuccess}
                  onLoadError={onDocumentLoadError}
                  loading={<div className={styles.loading}>Loading PDF...</div>}
                >
                  {Array.from(new Array(numPages), (el, index) => (
                    <Page
                      key={`page_${index + 1}`}
                      pageNumber={index + 1}
                      renderTextLayer={true}
                      renderAnnotationLayer={true}
                      width={typeof window !== "undefined" ? Math.min(window.innerWidth * 0.9, 940) : 800}
                      className={styles.pdfPage}
                    />
                  ))}
                </Document>
              </div>
            ) : isImage ? (
              <div className={styles.imageView}>
                <img src={fullUrl} alt={currentFile.label} className={styles.image} />
              </div>
            ) : (
              <CodeBlock language={extension} showLineNumbers>
                {fileContents[activeIndex] || "Loading..."}
              </CodeBlock>
            )}
          </div>

          <div className={styles.modalFooter}>
            <a href={fullUrl} download={currentFile.label} className={`${styles.button} ${styles.downloadButton}`}>
              Download {sourceList.length > 1 ? "Selected" : "File"}
            </a>
            <button onClick={() => setIsOpen(false)} className={`${styles.button} ${styles.cancelButton}`}>
              Close
            </button>
          </div>
        </div>
      </div>
    ) : null;

  return (
    <div className={styles.footerContainer}>
      <p className={styles.footerText}>
        <span className={styles.label}>
          {sourceList.length > 1 ? "Source files: " : "Source file: "}
          {sourceList.map((src, idx) => (
            <span key={idx}>
              <a href="#" onClick={(e) => { e.preventDefault(); setIsOpen(true); setActiveIndex(idx); }} className={styles.link}>
                {src.label}
              </a>
              {idx < sourceList.length - 1 ? ", " : ""}
            </span>
          ))}
        </span>
      </p>
      {modalElement && createPortal(modalElement, document.body)}
    </div>
  );
}
