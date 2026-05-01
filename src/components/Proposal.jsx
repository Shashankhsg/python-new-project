import { useState } from 'react'
import './Proposal.css'

function Proposal({ onResponse, isLoading }) {
  const [noButtonPosition, setNoButtonPosition] = useState({ top: 0, left: 0 })
  const [hoveredNo, setHoveredNo] = useState(false)
  const [showNoWarning, setShowNoWarning] = useState(false)

  const moveNoButton = () => {
    const randomTop = Math.floor(Math.random() * (window.innerHeight - 100))
    const randomLeft = Math.floor(Math.random() * (window.innerWidth - 100))
    setNoButtonPosition({ top: randomTop, left: randomLeft })
  }

  const handleNoMouseEnter = () => {
    moveNoButton()
    setHoveredNo(true)
    setShowNoWarning(true)
  }

  const handleNoMouseLeave = () => {
    setHoveredNo(false)
  }

  const handleNoClick = (e) => {
    e.preventDefault()
    moveNoButton()
    setHoveredNo(true)
    setShowNoWarning(true)
  }

  return (
    <div className="proposal-container">
      <div className="hearts-top">
        <span className="heart">💕</span>
        <span className="heart">💖</span>
        <span className="heart">💗</span>
        <span className="heart">💝</span>
      </div>

      <div className="proposal-content">
        <h1>I think we have a really good connection!!</h1>
        
        <div className="proposal-message">
          <p>
          To be Honest, this is the first time I’ve liked someone like this, and it’s you.
I was a little scared to say it because I didn’t want to spoil what we have.
I’m not very good at flirting, and if I ever irritated you, I’m sorry.
You’re a frontend developer and I’m a backend developer—I feel like we’re a perfect match.
I’ve started liking you, and I’d like to talk more and see where this goes.
If you feel the same, we can take it forward—no pressure.
          </p>
          <p className="heart-message">❤️</p>
        </div>

        <div className="proposal-buttons">
          <button 
            className="btn btn-yes-proposal" 
            onClick={() => onResponse(true)}
            disabled={isLoading}
          >
            {isLoading ? '⏳ Processing...' : '😍 Yes! 😍'}
          </button>
          
          <div 
            className={`no-button-wrapper ${hoveredNo ? 'moving' : ''}`}
            style={{
              position: noButtonPosition.top !== 0 || noButtonPosition.left !== 0 ? 'fixed' : 'relative',
              top: noButtonPosition.top !== 0 ? `${noButtonPosition.top}px` : 'auto',
              left: noButtonPosition.left !== 0 ? `${noButtonPosition.left}px` : 'auto',
            }}
          >
            <button 
              className="btn btn-no-proposal"
              onMouseEnter={handleNoMouseEnter}
              onMouseLeave={handleNoMouseLeave}
              onClick={handleNoClick}
              disabled={false}
            >
              No
            </button>
          </div>
        </div>
        {showNoWarning && (
          <p className="no-warning">please dont do this</p>
        )}
      </div>

      <div className="hearts-bottom">
        <span className="heart">💕</span>
        <span className="heart">💖</span>
        <span className="heart">💗</span>
        <span className="heart">💝</span>
      </div>
    </div>
  )
}

export default Proposal
