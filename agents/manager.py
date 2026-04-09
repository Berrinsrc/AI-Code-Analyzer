from crewai import Agent, Task

class AnalysisManager:
    def __init__(self, kod_icerigi):
        self.kod_icerigi = kod_icerigi

    def ajanlari_olustur(self):
        analiz_ajani = Agent(
            role='Senior Performance Architect & Code Auditor',
            goal='Analyze the logic of the provided code, identify bottlenecks, and suggest high-performance optimizations.',
            backstory='You have spent 20 years optimizing high-traffic systems at companies like NVIDIA and Google. You have a "hawk eye" for inefficient loops, redundant memory allocations, and slow algorithms. Your mission is to make every line of code run as fast and clean as possible.',
            llm='ollama/llama3',
            verbose=True,
            allow_delegation=False
        )

        editor_ajani = Agent(
            role='Technical Editor & Turkish Language Expert',
            goal='Review the performance analysis report and polish the Turkish language.',
            backstory='You are an expert technical writer fluent in both English and Turkish. Your specialty is taking AI-generated technical content and making it sound natural, professional, and grammatically perfect in Turkish.',
            llm='ollama/llama3',
            verbose=True,
            allow_delegation=False
        )
        return analiz_ajani, editor_ajani

    def gorevleri_olustur(self, analiz_ajani, editor_ajani):
        analiz_gorevi = Task(
            description=f"""
            1. Analyze the logic of the following Python code content:
            {self.kod_icerigi}  
            
            2. Identify efficiency issues, specifically focusing on the nested loops.
            3. Suggest a more performant way (e.g., using a Set or Dictionary).
            4. Provide the final optimized code block.
            """,
            expected_output="""
            Strictly follow these rules for the final report:
            - The entire report MUST be in professional Turkish.
            - Do NOT invent new words like 'Birçık'; use 'Çıktı' or 'Sonuç'.
            - Use clear headings: ## 1. Kodun Amacı, ## 2. Performans Sorunları, ## 3. İyileştirilmiş Kod Bloğu.
            - Keep technical terms (Big O, nested loops) in English if there is no clear Turkish equivalent.
            """,
            agent=analiz_ajani
        )

        editor_gorevi = Task(
            description="""
            1. Review the performance report provided by the Senior Performance Architect.
            2. Fix any grammar mistakes and unnatural Turkish phrasing (e.g., replace 'Birçık' with 'Sonuç').
            3. Ensure technical terms are consistent (e.g., use 'performans' instead of 'performance').
            4. Make the final report look like it was written by a human expert.
            """,
            expected_output="A perfectly polished, professional technical analysis report in Turkish.",
            agent=editor_ajani,
            context=[analiz_gorevi]
        )
        return analiz_gorevi, editor_gorevi