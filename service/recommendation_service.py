{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "64603624-58e2-4a40-ae1b-3d454b6ffaf3",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "import mlflow.pyfunc\n",
    "import pandas as pd\n",
    "from databricks import sql\n",
    "\n",
    "class RecommendationService:\n",
    "    def __init__(self, model_uri):\n",
    "        self.model_uri = model_uri\n",
    "        self.model = mlflow.pyfunc.load_model(model_uri)\n",
    "    \n",
    "    def recommend(self, movie_history_list):\n",
    "        \"\"\"\n",
    "        movie_history_list: List[int] 형태의 MovieLens movieId 리스트 입력\n",
    "        추천된 MovieLens movieId 리스트 반환\n",
    "        \"\"\"\n",
    "        input_df = pd.DataFrame({\"movie_history\": [movie_history_list]})\n",
    "        result = self.model.predict(input_df)\n",
    "        # result가 DataFrame 형식이고, 추천 리스트가 첫 행 첫 열에 있다고 가정\n",
    "        recommended_ids = result.iloc[0, 0]\n",
    "        return recommended_ids\n",
    "\n",
    "\n",
    "def get_tmdb_id_from_movie_id(movie_id, connection_params):\n",
    "    import logging\n",
    "    try:\n",
    "        with sql.connect(**connection_params) as connection:\n",
    "            cursor = connection.cursor()\n",
    "            query = f\"SELECT tmdbId FROM `1dt_team8_databricks`.`movielens-32m`.links WHERE movieId = {movie_id}\"\n",
    "            cursor.execute(query)\n",
    "            result = cursor.fetchone()\n",
    "            cursor.close()\n",
    "            if result:\n",
    "                return result[0]\n",
    "            else:\n",
    "                logging.warning(f\"MovieLens movieId {movie_id}에 대한 tmdbId를 찾을 수 없습니다.\")\n",
    "                return None\n",
    "    except Exception as e:\n",
    "        logging.error(f\"Databricks SQL 연결 오류: {e}\")\n",
    "        return None"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "2"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "mlflow_model_load_test",
   "widgets": {}
  },
  "kernelspec": {
   "display_name": "",
   "name": ""
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
