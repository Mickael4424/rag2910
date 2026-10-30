"""command line interface for the RAG Pipeline."""


class RagCLI:
    """RAG commands through Python Fire."""

    def index(self, max_chunk_size: int = 2000) -> None:
        """Chunk data raw and build the index under data/processed/.

        Args:
            max_chunk_size: maximum size of the chunk
        """
        print(f"Index size: {max_chunk_size}")

    def search(self, query: str, k: int = 10) -> None:
        """Search the top-k sources for a single query.

        Args:
            query: the question to search for
            k: number of sources to return
        """
        print(f"search: query={query!r}, k={k}")

    def search_dataset(self,
                       dataset_path: str,
                       save_directory: str,
                       k: int = 10
                       ) -> None:
        """
        Run search over a whole dataset and
        write a StudentSearchResults JSON file.

        Args:
            dataset_path: path of the dataset file
            save_directory: path of the saving directory
            k: number of sources to return
        """
        print(
            f"search dataset: dataset_path={dataset_path}, "
            f"k={k}, save directory={save_directory}"
            )

    def answer(self,
               query: str,
               k: int = 10) -> None:
        """Answer a single query using the retrieved context.
        Args:
            query: the question to search for
            k: number of sources to return
        """
        print(f"answer: query={query!r}, k={k}")

    def answer_dataset(self,
                       student_search_results_path: str,
                       save_directory: str
                       ) -> None:
        """Generate answers for a dataset,
            producing a StudentSearchResultsAndAnswer JSON file
        Args:
            student_search_results_path: .
            save_directory: path of the saving directory
        """
        print(
            f"answer dataset: student_search_results_path="
            f"{student_search_results_path}, "
            f"save directory={save_directory}"
            )

    def evaluate(self,
                 student_search_results_path: str,
                 dataset_path: str
                 ) -> None:
        """
        Report your own recall@k against a ground-truth dataset,
        for your own testing.

        Args:
            student_search_results_path: path to the StudentSearchResults
                JSON produced by search_dataset
            dataset_path: path to the AnsweredQuestions ground-truth dataset.
        """
        print(f"evaluate: "
              f"student search results path="
              f"{student_search_results_path}, "
              f"dataset path={dataset_path}"
              )
