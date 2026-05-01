import { useState } from 'react'
import './Proposal.css'

function Proposal({ onResponse, isLoading }) {
  const [noButtonPosition, setNoButtonPosition] = useState({ top: 0, left: 0 })
  const [hoveredNo, setHoveredNo] = useState(false)

  const moveNoButton = () => {
    const randomTop = Math.floor(Math.random() * (window.innerHeight - 100))
    const randomLeft = Math.floor(Math.random() * (window.innerWidth - 100))
    setNoButtonPosition({ top: randomTop, left: randomLeft })
  }

  const handleNoMouseEnter = () => {
    moveNoButton()
    setHoveredNo(true)
  }

  const handleNoMouseLeave = () => {
    setHoveredNo(false)
  }

  const handleNoClick = (e) => {
    e.preventDefault()
    moveNoButton()
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
        <h1>💕 Will you be my girlfriend? 💕</h1>
        
        <div className="proposal-message">
          <p>
            You are the most amazing person I've ever met. Your smile brightens my day, 
            and I can't stop thinking about you. I would be the happiest person if you 
            would say yes and let me be a part of your life.
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
