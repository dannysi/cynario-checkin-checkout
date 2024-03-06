from fastapi import FastAPI
from controller.task_controller import router as task_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
app.include_router(task_router)