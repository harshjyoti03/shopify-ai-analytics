require "net/http"
require "json"

module Api
  module V1
    class QuestionsController < ApplicationController
      def create
        uri = URI("http://localhost:8000/ask")

        http = Net::HTTP.new(uri.host, uri.port)
        request = Net::HTTP::Post.new(uri.path)
        request["Content-Type"] = "application/json"

        request.body = {
          store_id: params[:store_id],
          question: params[:question]
        }.to_json

        response = http.request(request)

        render json: JSON.parse(response.body)
      end
    end
  end
end
