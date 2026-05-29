```javascript
let todoList = [];
let id = 0;

document.addEventListener('DOMContentLoaded', function() {
    const todoInput = document.getElementById('todo-input');
    const todoButton = document.getElementById('todo-button');
    const todoListElement = document.getElementById('todo-list');

    todoButton.addEventListener('click', function() {
        const todoText = todoInput.value.trim();
        if (todoText) {
            const todoItem = {
                id: id,
                text: todoText,
                completed: false
            };
            todoList.push(todoItem);
            renderTodoList();
            todoInput.value = '';
            id++;
        }
    });

    todoListElement.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-button')) {
            const todoItemId = parseInt(event.target.dataset.id);
            todoList = todoList.filter(function(item) {
                return item.id !== todoItemId;
            });
            renderTodoList();
        } else if (event.target.classList.contains('todo-text')) {
            const todoItemId = parseInt(event.target.dataset.id);
            const todoItem = todoList.find(function(item) {
                return item.id === todoItemId;
            });
            if (todoItem) {
                todoItem.completed = !todoItem.completed;
                renderTodoList();
            }
        }
    });
});

function renderTodoList() {
    const todoListElement = document.getElementById('todo-list');
    todoListElement.innerHTML = '';
    todoList.forEach(function(todoItem) {
        const todoListItem = document.createElement('li');
        todoListItem.classList.add('todo-list-item');
        const todoText = document.createElement('span');
        todoText.classList.add('todo-text');
        todoText.textContent = todoItem.text;
        todoText.dataset.id = todoItem.id;
        if (todoItem.completed) {
            todoText.style.textDecoration = 'line-through';
        }
        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-button');
        deleteButton.textContent = 'Delete';
        deleteButton.dataset.id = todoItem.id;
        todoListItem.appendChild(todoText);
        todoListItem.appendChild(deleteButton);
        todoListElement.appendChild(todoListItem);
    });
}
```