import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter.font as tkFont


class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Game state
        self.board = [' '] * 9
        self.current_player = 'X'
        self.player1_name = ''
        self.player2_name = ''
        self.game_started = False
        self.game_over = False
        self.winner = ''
        self.move_count = 0
        
        # Colors and styles
        self.bg_color = "#4A90E2"
        self.card_color = "#FFFFFF"
        self.button_color = "#E3F2FD"
        self.hover_color = "#BBDEFB"
        self.x_color = "#2196F3"
        self.o_color = "#F44336"
        self.win_color = "#4CAF50"
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Fonts
        self.title_font = tkFont.Font(family="Arial", size=24, weight="bold")
        self.button_font = tkFont.Font(family="Arial", size=20, weight="bold")
        self.label_font = tkFont.Font(family="Arial", size=14, weight="bold")
        self.small_font = tkFont.Font(family="Arial", size=12)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        self.main_frame = tk.Frame(self.root, bg=self.card_color, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="Tic-Tac-Toe",
            font=self.title_font,
            bg=self.card_color,
            fg="#333333"
        )
        self.title_label.pack(pady=(0, 20))
        
        # Setup name input screen
        self.setup_name_input()
    
    def setup_name_input(self):
        """Setup the name input interface"""
        self.name_frame = tk.Frame(self.main_frame, bg=self.card_color)
        self.name_frame.pack(expand=True, fill='both')
        
        # Player 1 input
        tk.Label(
            self.name_frame,
            text="Player 1 Name (X):",
            font=self.label_font,
            bg=self.card_color,
            fg="#666666"
        ).pack(pady=(20, 5))
        
        self.player1_entry = tk.Entry(
            self.name_frame,
            font=self.small_font,
            width=30,
            relief='solid',
            borderwidth=2
        )
        self.player1_entry.pack(pady=(0, 20))
        
        # Player 2 input
        tk.Label(
            self.name_frame,
            text="Player 2 Name (O):",
            font=self.label_font,
            bg=self.card_color,
            fg="#666666"
        ).pack(pady=(0, 5))
        
        self.player2_entry = tk.Entry(
            self.name_frame,
            font=self.small_font,
            width=30,
            relief='solid',
            borderwidth=2
        )
        self.player2_entry.pack(pady=(0, 30))
        
        # Start game button
        self.start_button = tk.Button(
            self.name_frame,
            text="Start Game",
            font=self.label_font,
            bg="#4CAF50",
            fg="white",
            relief='flat',
            padx=40,
            pady=10,
            command=self.start_game,
            cursor="hand2"
        )
        self.start_button.pack()
        
        # Bind Enter key to start game
        self.root.bind('<Return>', lambda e: self.start_game())
    
    def start_game(self):
        """Start the game with entered names"""
        name1 = self.player1_entry.get().strip()
        name2 = self.player2_entry.get().strip()
        
        if not name1 or not name2:
            messagebox.showerror("Error", "Please enter both player names!")
            return
        
        self.player1_name = name1
        self.player2_name = name2
        self.game_started = True
        
        # Clear name input and setup game board
        self.name_frame.destroy()
        self.setup_game_board()
    
    def setup_game_board(self):
        """Setup the game board interface"""
        # Player info frame
        self.info_frame = tk.Frame(self.main_frame, bg=self.card_color)
        self.info_frame.pack(fill='x', pady=(0, 20))
        
        # Player names display
        self.players_frame = tk.Frame(self.info_frame, bg=self.card_color)
        self.players_frame.pack()
        
        tk.Label(
            self.players_frame,
            text=f"{self.player1_name} (X)",
            font=self.label_font,
            bg=self.card_color,
            fg=self.x_color
        ).pack(side='left', padx=20)
        
        tk.Label(
            self.players_frame,
            text="VS",
            font=self.label_font,
            bg=self.card_color,
            fg="#666666"
        ).pack(side='left', padx=10)
        
        tk.Label(
            self.players_frame,
            text=f"{self.player2_name} (O)",
            font=self.label_font,
            bg=self.card_color,
            fg=self.o_color
        ).pack(side='left', padx=20)
        
        # Current player display
        self.current_player_label = tk.Label(
            self.info_frame,
            text="",
            font=self.label_font,
            bg=self.card_color,
            fg=self.x_color
        )
        self.current_player_label.pack(pady=(10, 0))
        
        # Game board
        self.board_frame = tk.Frame(self.main_frame, bg=self.card_color)
        self.board_frame.pack(pady=20)
        
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            
            button = tk.Button(
                self.board_frame,
                text="",
                font=self.button_font,
                width=4,
                height=2,
                bg=self.button_color,
                relief='solid',
                borderwidth=2,
                command=lambda idx=i: self.handle_cell_click(idx),
                cursor="hand2"
            )
            button.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(button)
        
        # Control buttons frame
        self.controls_frame = tk.Frame(self.main_frame, bg=self.card_color)
        self.controls_frame.pack(pady=20)
        
        self.reset_button = tk.Button(
            self.controls_frame,
            text="Reset Game",
            font=self.small_font,
            bg="#4CAF50",
            fg="white",
            relief='flat',
            padx=20,
            pady=8,
            command=self.reset_game,
            cursor="hand2"
        )
        self.reset_button.pack(side='left', padx=(0, 10))
        
        self.new_game_button = tk.Button(
            self.controls_frame,
            text="New Game",
            font=self.small_font,
            bg="#757575",
            fg="white",
            relief='flat',
            padx=20,
            pady=8,
            command=self.new_game,
            cursor="hand2"
        )
        self.new_game_button.pack(side='left')
        
        # Update display
        self.update_current_player_display()
    
    def check_winner(self, board):
        """Check if there's a winner on the board"""
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for pattern in win_patterns:
            a, b, c = pattern
            if board[a] != ' ' and board[a] == board[b] == board[c]:
                return board[a]
        return None
    
    def handle_cell_click(self, index):
        """Handle clicking on a game board cell"""
        if self.board[index] != ' ' or self.game_over:
            return
        
        # Make the move
        self.board[index] = self.current_player
        self.move_count += 1
        
        # Update button display
        color = self.x_color if self.current_player == 'X' else self.o_color
        self.buttons[index].config(
            text=self.current_player,
            fg=color,
            bg=self.hover_color,
            state='disabled'
        )
        
        # Check for winner
        winner_player = self.check_winner(self.board)
        
        if winner_player:
            self.winner = self.player1_name if self.current_player == 'X' else self.player2_name
            self.game_over = True
            self.show_game_over()
        elif self.move_count == 9:
            self.winner = 'Tie'
            self.game_over = True
            self.show_game_over()
        else:
            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.update_current_player_display()
    
    def update_current_player_display(self):
        """Update the current player display"""
        if not self.game_over:
            current_name = self.player1_name if self.current_player == 'X' else self.player2_name
            color = self.x_color if self.current_player == 'X' else self.o_color
            self.current_player_label.config(
                text=f"Current Player: {current_name} ({self.current_player})",
                fg=color
            )
    
    def show_game_over(self):
        """Show game over message"""
        # Update current player label to show result
        if self.winner == 'Tie':
            self.current_player_label.config(
                text="Game Tied! 🤝",
                fg="#FF9800"
            )
            messagebox.showinfo("Game Over", "It's a tie! 🤝")
        else:
            self.current_player_label.config(
                text=f"{self.winner} Wins! 🎉",
                fg=self.win_color
            )
            messagebox.showinfo("Game Over", f"🎉 {self.winner} Wins! 🎉")
        
        # Disable all buttons
        for button in self.buttons:
            button.config(state='disabled')
    
    def reset_game(self):
        """Reset the current game"""
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_over = False
        self.winner = ''
        self.move_count = 0
        
        # Reset all buttons
        for button in self.buttons:
            button.config(
                text="",
                bg=self.button_color,
                fg="black",
                state='normal'
            )
        
        self.update_current_player_display()
    
    def new_game(self):
        """Start a completely new game"""
        # Reset all game state
        self.board = [' '] * 9
        self.current_player = 'X'
        self.player1_name = ''
        self.player2_name = ''
        self.game_started = False
        self.game_over = False
        self.winner = ''
        self.move_count = 0
        
        # Clear the current interface
        for widget in self.main_frame.winfo_children():
            if widget != self.title_label:
                widget.destroy()
        
        # Setup name input again
        self.setup_name_input()
    
    def run(self):
        """Start the GUI application"""
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
        
        self.root.mainloop()


# Function to start the GUI game
def main():
    """Main function to start the game"""
    game = TicTacToeGUI()
    game.run()


# Run the game if this file is executed directly
if __name__ == "__main__":
    main()
