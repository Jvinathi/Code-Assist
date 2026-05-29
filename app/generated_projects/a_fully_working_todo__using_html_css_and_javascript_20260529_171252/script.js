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
            const todoItemId = event.target.dataset.id;
            todoList = todoList.filter(function(item) {
                return item.id !== parseInt(todoItemId);
            });
            renderTodoList();
        } else if (event.target.classList.contains('todo-text')) {
            const todoItemId = event.target.dataset.id;
            const todoItem = todoList.find(function(item) {
                return item.id === parseInt(todoItemId);
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
        const todoTextElement = document.createElement('span');
        todoTextElement.classList.add('todo-text');
        todoTextElement.textContent = todoItem.text;
        todoTextElement.dataset.id = todoItem.id;
        if (todoItem.completed) {
            todoTextElement.style.textDecoration = 'line-through';
        }
        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-button');
        deleteButton.textContent = 'Delete';
        deleteButton.dataset.id = todoItem.id;
        todoListItem.appendChild(todoTextElement);
        todoListItem.appendChild(deleteButton);
        todoListElement.appendChild(todoListItem);
    });
}
```